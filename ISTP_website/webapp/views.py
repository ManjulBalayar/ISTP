from django.shortcuts import render
from webapp.models import Qol, Qol1994, Qol2004
from .models_soc1994 import Soc1994
from .models_soc2004 import Soc2004
from .models_soc2014 import Soc2014
import pandas as pd
from django.http import JsonResponse, HttpResponse
import logging
from django.db.models import Q
from django_ratelimit.decorators import ratelimit
from django.core.exceptions import PermissionDenied
from .utils import safe_values, safe_values_list

# Setup proper structured logging
logger = logging.getLogger('webapp')

def ratelimited_error(request, exception):
    """Handle rate limit exceptions"""
    logger.warning(f"Rate limit exceeded for {request.META.get('REMOTE_ADDR')}")
    return HttpResponse("Too many requests, please try again later.", status=429)

@ratelimit(key='ip', rate='10/m')
def home(request):
    logger.info(f"Home page accessed by {request.META.get('REMOTE_ADDR')}")
    return render(request, 'app/home.html')

@ratelimit(key='ip', rate='20/m')
def index(request):
    logger.info(f"Data page accessed by {request.META.get('REMOTE_ADDR')}")
    try:
        # Using safe_values_list instead of values_list to prevent SQL injection
        towns = safe_values_list(Qol.objects.all(), 'name', flat=True).distinct()
        demographics = ['ALL', 'AGE', 'SEX', 'TENURE', 'INCOME']
        qol_data_types = [
            'Jobs', 'Medical', 'Public School', 'Housing', 'Childcare',
            'Seniorcare', 'Youth Programs', 'Community Services Overall',
            'Recreation and Entertainment', 'Police', 'Fire',
            'Condition of Streets', 'Condition of Parks', 'Garbage Collection',
            'Water', 'Government Services Overall'
        ]
        social_capital_data_types = [
            'Friends in Town', 'Relatives in Town', 'Supportiveness', 
            'Organizations Working Together', 'New Residents as Leaders',
            'Open to Ideas', 'Local Organization Membership', 'Outside Organization Membership',
            'Activity Level in Organizations', 'Local vs Outside Organizations',
            'Volunteer Participation', 'Town Support for Projects', 'Involvement in Decisions',
            'Sorry to Leave', 'Feel at Home', 'Town Like Friends', 'Go-for-it Attitude',
            'Well-kept Property', 'Looking Out for Self'
        ]
        
        data_types = [
            {'id': 'qol', 'name': 'Quality of Life'},
            {'id': 'soc', 'name': 'Social Capital'}
        ]
        
        logger.debug(f"Retrieved {len(towns)} towns for data page")
        return render(request, 'app/data.html', {
            'towns': towns,
            'demographics': demographics,
            'qol_data_types': qol_data_types,
            'social_capital_data_types': social_capital_data_types,
            'data_types': data_types
        })
    except Exception as e:
        logger.error(f"Error in index view: {str(e)}", exc_info=True)
        return render(request, 'app/error.html', {'error_message': 'An error occurred. Please try again later.'})


@ratelimit(key='ip', rate='30/m')
def get_specific_demographic_options(request):
    main_demographic = request.GET.get('demographic', None)

    # Map main demographic categories to their corresponding specific categories in the CAT column
    demographic_mapping = {
        'ALL': ['ALL'],
        'AGE': ['AGE1', 'AGE2', 'AGE3'],
        'SEX': ['SEX1M', 'SEX1F'],
        'TENURE': ['TENURE1', 'TENURE2', 'TENURE3'],
        'INCOME': ['INC1', 'INC2', 'INC3', 'INC4']
    }

    # Define a dictionary for human-readable labels
    human_readable_labels = {
        'ALL': 'All respondents',
        'AGE1': '18-44 years',
        'AGE2': '45-64 years',
        'AGE3': '65 years and older',
        'SEX1M': 'Men',
        'SEX1F': 'Women',
        'TENURE1': 'Lived in town 1-9 years',
        'TENURE2': 'Lived in town 10-19 years',
        'TENURE3': 'Lived in town 20 years or more',
        'INC1': 'Income in the 1st-19th percentile',
        'INC2': 'Income in the 20th-49th percentile',
        'INC3': 'Income in the 50th-79th percentile',
        'INC4': 'Income in the 80th-99th percentile'
    }

    # Get specific categories based on the selected main demographic
    specific_categories = demographic_mapping.get(main_demographic, [])

    # Convert these categories to their human-readable form
    specific_options = [human_readable_labels.get(category, category) for category in specific_categories]

    return JsonResponse({'specific_options': specific_options})


@ratelimit(key='ip', rate='30/m')
def get_qol_data_options(request):
    town = request.GET.get('town', None)
    specific_demographic = request.GET.get('specific_demographic', None)
    
    logger.info(f"QOL data requested for town: {town}, demographic: {specific_demographic}")

    # Validate input parameters
    if not town or not specific_demographic:
        logger.warning(f"Invalid parameters: town={town}, demographic={specific_demographic}")
        return JsonResponse({'error': 'Missing required parameters'}, status=400)
    
    # Prevent potential injection by validating against allowed values
    allowed_demographics = ['ALL', 'AGE1', 'AGE2', 'AGE3', 'SEX1M', 'SEX1F', 
                           'TENURE1', 'TENURE2', 'TENURE3', 'INC1', 'INC2', 'INC3', 'INC4']
    
    if specific_demographic not in allowed_demographics:
        logger.warning(f"Invalid demographic parameter: {specific_demographic}")
        return JsonResponse({'error': 'Invalid demographic parameter'}, status=400)

    try:
        # Use the ORM properly to prevent SQL injection
        qol_data = Qol.objects.filter(name=town, cat=specific_demographic).first()
        
        if not qol_data:
            logger.warning(f"No QOL data found for town: {town}, demographic: {specific_demographic}")
            return JsonResponse({'error': 'No data found for the selected options.'})

        qol_ratings = {
            'jobs_vg': qol_data.qoljobs_vg,
            'jobs_g': qol_data.qoljobs_g,
            'jobs_f': qol_data.qoljobs_f,
            'jobs_p': qol_data.qoljobs_p,
            'jobs_dnk': qol_data.qoljobs_dnk,
            'jobs_na': qol_data.qoljobs_na,
            'medical_vg': qol_data.qolmedical_vg,
            'medical_g': qol_data.qolmedical_g,
            'medical_f': qol_data.qolmedical_f,
            'medical_p': qol_data.qolmedical_p,
            'medical_dnk': qol_data.qolmedical_dnk,
            'medical_na': qol_data.qolmedical_na,
            'k12_vg': qol_data.qolk12_vg,
            'k12_g': qol_data.qolk12_g,
            'k12_f': qol_data.qolk12_f,
            'k12_p': qol_data.qolk12_p,
            'k12_dnk': qol_data.qolk12_dnk,
            'k12_na': qol_data.qolk12_na,
            'housing_vg': qol_data.qolhousing_vg,
            'housing_g': qol_data.qolhousing_g,
            'housing_f': qol_data.qolhousing_f,
            'housing_p': qol_data.qolhousing_p,
            'housing_dnk': qol_data.qolhousing_dnk,
            'housing_na': qol_data.qolhousing_na,
            'shop_vg': qol_data.qolshop_vg,
            'shop_g': qol_data.qolshop_g,
            'shop_f': qol_data.qolshop_f,
            'shop_p': qol_data.qolshop_p,
            'shop_dnk': qol_data.qolshop_dnk,
            'shop_na': qol_data.qolshop_na,
            'childcare_vg': qol_data.qolchildcare_vg,
            'childcare_g': qol_data.qolchildcare_g,
            'childcare_f': qol_data.qolchildcare_f,
            'childcare_p': qol_data.qolchildcare_p,
            'childcare_dnk': qol_data.qolchildcare_dnk,
            'childcare_na': qol_data.qolchildcare_na,
            'seniorcare_vg': qol_data.qolseniorcare_vg,
            'seniorcare_g': qol_data.qolseniorcare_g,
            'seniorcare_f': qol_data.qolseniorcare_f,
            'seniorcare_p': qol_data.qolseniorcare_p,
            'seniorcare_dnk': qol_data.qolseniorcare_dnk,
            'seniorcare_na': qol_data.qolseniorcare_na,
            'youth_vg': qol_data.qolyouth_vg,
            'youth_g': qol_data.qolyouth_g,
            'youth_f': qol_data.qolyouth_f,
            'youth_p': qol_data.qolyouth_p,
            'youth_dnk': qol_data.qolyouth_dnk,
            'youth_na': qol_data.qolyouth_na,
            'commsrvall_vg': qol_data.qolcommsrvall_vg,
            'commsrvall_g': qol_data.qolcommsrvall_g,
            'commsrvall_f': qol_data.qolcommsrvall_f,
            'commsrvall_p': qol_data.qolcommsrvall_p,
            'commsrvall_dnk': qol_data.qolcommsrvall_dnk,
            'commsrvall_na': qol_data.qolcommsrvall_na,
            'recrentr_vg': qol_data.qolrecrentr_vg,
            'recrentr_g': qol_data.qolrecrentr_g,
            'recrentr_f': qol_data.qolrecrentr_f,
            'recrentr_p': qol_data.qolrecrentr_p,
            'recrentr_dnk': qol_data.qolrecrentr_dnk,
            'recrentr_na': qol_data.qolrecrentr_na,
            'police_vg': qol_data.qolpolice_vg,
            'police_g': qol_data.qolpolice_g,
            'police_p': qol_data.qolpolice_p,
            'police_f': qol_data.qolpolice_f,
            'police_dnk': qol_data.qolpolice_dnk,
            'police_na': qol_data.qolpolice_na,
            'fire_vg': qol_data.qolfire_vg,
            'fire_g': qol_data.qolfire_g,
            'fire_f': qol_data.qolfire_f,
            'fire_p': qol_data.qolfire_p,
            'fire_dnk': qol_data.qolfire_dnk,
            'fire_na': qol_data.qolfire_na,
            'ems_vg': qol_data.qolems_vg,
            'ems_g': qol_data.qolems_g,
            'ems_f': qol_data.qolems_f,
            'ems_p': qol_data.qolems_p,
            'ems_dnk': qol_data.qolems_dnk,
            'ems_na': qol_data.qolems_na,
            'streets_vg': qol_data.qolstreets_vg,
            'streets_g': qol_data.qolstreets_g,
            'streets_f': qol_data.qolstreets_f,
            'streets_p': qol_data.qolstreets_p,
            'streets_dnk': qol_data.qolstreets_dnk,
            'streets_na': qol_data.qolstreets_na,
            'parks_vg': qol_data.qolparks_vg,
            'parks_g': qol_data.qolparks_g,
            'parks_f': qol_data.qolparks_f,
            'parks_p': qol_data.qolparks_p,
            'parks_dnk': qol_data.qolparks_dnk,
            'parks_na': qol_data.qolparks_na,
            'garbage_vg': qol_data.qolgarbage_vg,
            'garbage_g': qol_data.qolgarbage_g,
            'garbage_f': qol_data.qolgarbage_f,
            'garbage_p': qol_data.qolgarbage_p,
            'garbage_dnk': qol_data.qolgarbage_dnk,
            'garbage_na': qol_data.qolgarbage_na,
            'water_vg': qol_data.qolwater_vg,
            'water_g': qol_data.qolwater_g,
            'water_f': qol_data.qolwater_f,
            'water_p': qol_data.qolwater_p,
            'water_dnk': qol_data.qolwater_dnk,
            'water_na': qol_data.qolwater_na,
            'govtsrvall_vg': qol_data.qolgovtsrvall_vg,
            'govtsrvall_g': qol_data.qolgovtsrvall_g,
            'govtsrvall_f': qol_data.qolgovtsrvall_f,
            'govtsrvall_p': qol_data.qolgovtsrvall_p,
            'govtsrvall_dnk': qol_data.qolgovtsrvall_dnk,
            'govtsrvall_na': qol_data.qolgovtsrvall_na,
        }

        logger.debug(f"Successfully retrieved QOL data for {town}, {specific_demographic}")
        return JsonResponse({'qol_ratings': qol_ratings})
    except Exception as e:
        logger.error(f"Error retrieving QOL data for {town}, {specific_demographic}: {str(e)}", exc_info=True)
        return JsonResponse({'error': f'Error retrieving data: {str(e)}'})

@ratelimit(key='ip', rate='30/m')
def search_towns(request):
    term = request.GET.get('term', '')
    logger.info(f"Town search for term: '{term}'")
    
    # Validate search term
    if len(term) > 100:  # Prevent excessively long search terms
        logger.warning(f"Excessively long search term ({len(term)} chars) from {request.META.get('REMOTE_ADDR')}")
        return JsonResponse({'error': 'Search term too long'}, status=400)
    
    try:
        # Use safe_values_list instead of values_list
        towns = safe_values_list(Qol.objects.filter(name__icontains=term), 'name', flat=True).distinct()
        logger.debug(f"Town search found {len(towns)} matches for '{term}'")
        return JsonResponse(list(towns), safe=False)
    except Exception as e:
        logger.error(f"Error in town search for '{term}': {str(e)}", exc_info=True)
        return JsonResponse({'error': 'Error performing search'}, status=500)

@ratelimit(key='ip', rate='20/m')
def query_data(request):
    try:
        town = request.GET.get('town')
        specific_demographic = request.GET.get('specific_demographic')
        data_type = request.GET.get('data_type')
        year = request.GET.get('year', '2014')  # Default to 2014

        logger.info(f"Year: {year}, Town: {town}, Demographic: {specific_demographic}, Data Type: {data_type}")
        
        # Validate input parameters
        if not town or not specific_demographic or not data_type:
            logger.warning(f"Missing parameters in query_data: town={town}, demographic={specific_demographic}, data_type={data_type}")
            return JsonResponse({'error': 'Missing required parameters'}, status=400)
            
        # Validate year
        allowed_years = ['1994', '2004', '2014', 'All']
        if year not in allowed_years:
            logger.warning(f"Invalid year parameter: {year}")
            return JsonResponse({'error': 'Invalid year parameter'}, status=400)

        # Handle different data types
        if data_type == 'qol':
            qol_data_type = request.GET.get('qol_data_type')
            if not qol_data_type:
                return JsonResponse({'error': 'Missing Quality of Life data type parameter'}, status=400)
            return query_qol_data(request, town, specific_demographic, qol_data_type, year)
        elif data_type == 'soc':
            soc_data_type = request.GET.get('soc_data_type')
            if not soc_data_type:
                return JsonResponse({'error': 'Missing Social Capital data type parameter'}, status=400)
            return query_social_capital_data(request, town, specific_demographic, soc_data_type, year)
        else:
            return JsonResponse({'error': 'Invalid data type selected.'}, status=400)
    except Exception as e:
        logger.error(f"Error querying data: {str(e)}")
        return JsonResponse({'error': 'An error occurred processing your request.'})

def query_qol_data(request, town, specific_demographic, qol_data_type, year):
    try:
        # Map years to their respective models
        model_mapping = {
            '1994': Qol1994,
            '2004': Qol2004,
            '2014': Qol
        }

        demographic_mapping = {
            'All respondents': 'ALL',
            '18-44 years': 'AGE1',
            '45-64 years': 'AGE2',
            '65 years and older': 'AGE3',
            'Men': 'SEX1M',
            'Women': 'SEX2F',
            'Lived in town 1-9 years': 'TENURE1',
            'Lived in town 10-19 years': 'TENURE2',
            'Lived in town 20 years or more': 'TENURE3',
            'Income in the 1st-19th percentile': 'INC1',
            'Income in the 20th-49th percentile': 'INC2',
            'Income in the 50th-79th percentile': 'INC3',
            'Income in the 80th-99th percentile': 'INC4'
        }

        QolModel = model_mapping.get(year, Qol)  # Use Qol as default if year is not recognized

        if not QolModel:
            raise ValueError(f"Invalid year: {year}")

        cat_value = demographic_mapping.get(specific_demographic, specific_demographic)

        qol_data = QolModel.objects.filter(name=town, cat=cat_value).values().first()
        if qol_data:
            qol_ratings = {key: qol_data[key] for key in qol_data if key.startswith(f'qol{qol_data_type.lower()}')}
            return JsonResponse({'qol_ratings': qol_ratings})
        else:
            return JsonResponse({'error': 'No data found for the selected options.'})
    except Exception as e:
        logger.error(f"Error querying QOL data: {str(e)}")
        return JsonResponse({'error': 'An error occurred processing your request.'})

def query_social_capital_data(request, town, specific_demographic, soc_data_type, year):
    try:
        # Map years to their respective models
        model_mapping = {
            '1994': Soc1994,
            '2004': Soc2004,
            '2014': Soc2014
        }

        # Map social capital data types to their field prefixes
        soc_prefix_mapping = {
            'Friends in Town': 'scfriends',
            'Relatives in Town': 'screlatives',
            'Supportiveness': 'scsupportive',
            'Organizations Working Together': 'scorgsworkall',
            'New Residents as Leaders': 'scnewresleader',
            'Open to Ideas': 'scopenideas',
            'Local Organization Membership': 'sclocalorg',
            'Outside Organization Membership': 'scoutsideorg',
            'Activity Level in Organizations': 'scactiveorg',
            'Local vs Outside Organizations': 'sclocoutorg',
            'Volunteer Participation': 'cevolunteer',
            'Town Support for Projects': 'cetowngetsbehind',
            'Involvement in Decisions': 'ceinvolvdecisions',
            'Sorry to Leave': 'casorryleave',
            'Feel at Home': 'cafeelhome',
            'Town Like Friends': 'catownlikefriends',
            'Go-for-it Attitude': 'csmoregoforit',
            'Well-kept Property': 'cswellkept',
            'Looking Out for Self': 'cslookoutforself'
        }

        demographic_mapping = {
            'All respondents': 'ALL',
            '18-44 years': 'AGE1',
            '45-64 years': 'AGE2',
            '65 years and older': 'AGE3',
            'Men': 'SEX1M',
            'Women': 'SEX2F',
            'Lived in town 1-9 years': 'TENURE1',
            'Lived in town 10-19 years': 'TENURE2',
            'Lived in town 20 years or more': 'TENURE3',
            'Income in the 1st-19th percentile': 'INC1',
            'Income in the 20th-49th percentile': 'INC2',
            'Income in the 50th-79th percentile': 'INC3',
            'Income in the 80th-99th percentile': 'INC4'
        }

        SocModel = model_mapping.get(year)
        if not SocModel:
            raise ValueError(f"Invalid year: {year}")

        cat_value = demographic_mapping.get(specific_demographic, specific_demographic)
        prefix = soc_prefix_mapping.get(soc_data_type)
        
        if not prefix:
            return JsonResponse({'error': 'Invalid Social Capital data type selected.'})

        soc_data = SocModel.objects.filter(name=town, cat=cat_value).values().first()
        
        if soc_data:
            soc_ratings = {key: soc_data[key] for key in soc_data if key.lower().startswith(prefix.lower())}
            return JsonResponse({'soc_ratings': soc_ratings})
        else:
            return JsonResponse({'error': 'No data found for the selected options.'})
    except Exception as e:
        logger.error(f"Error querying Social Capital data: {str(e)}")
        return JsonResponse({'error': 'An error occurred processing your request.'})