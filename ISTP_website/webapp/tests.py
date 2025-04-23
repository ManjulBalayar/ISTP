from django.test import TestCase, Client
from django.urls import reverse
from .models import Qol
import json

# Create your tests here.

class ViewsTestCase(TestCase):
    def setUp(self):
        # Create test data
        self.client = Client()
        self.home_url = reverse('home')
        self.index_url = reverse('index')
        
        # Create a test town
        Qol.objects.create(
            name='TestTown',
            cat='ALL',
            qoljobs_vg=10,
            qoljobs_g=20,
            qoljobs_f=30,
            qoljobs_p=30,
            qoljobs_dnk=5,
            qoljobs_na=5,
            qolmedical_vg=10,
            qolmedical_g=20,
            qolmedical_f=30,
            qolmedical_p=30,
            qolmedical_dnk=5,
            qolmedical_na=5,
            qolk12_vg=10,
            qolk12_g=20,
            qolk12_f=30,
            qolk12_p=30,
            qolk12_dnk=5,
            qolk12_na=5,
            # Add other required fields with sample data
        )
    
    def test_home_view(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/home.html')
    
    def test_index_view(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/data.html')
        self.assertIn('towns', response.context)
        self.assertIn('demographics', response.context)
        self.assertIn('qol_data_types', response.context)
    
    def test_search_towns(self):
        response = self.client.get(reverse('search_towns'), {'term': 'Test'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn('TestTown', data)
    
    def test_get_specific_demographic_options(self):
        response = self.client.get(reverse('get_specific_demographic_options'), {'demographic': 'AGE'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn('specific_options', data)
        self.assertEqual(len(data['specific_options']), 3)  # AGE has 3 subcategories
    
    def test_get_qol_data_options(self):
        response = self.client.get(reverse('get_qol_data_options'), {
            'town': 'TestTown',
            'specific_demographic': 'ALL'
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn('qol_ratings', data)
        self.assertEqual(data['qol_ratings']['jobs_vg'], 10)
        self.assertEqual(data['qol_ratings']['jobs_g'], 20)

class ModelTestCase(TestCase):
    def setUp(self):
        # Create sample data
        self.qol_data = Qol.objects.create(
            name='TestTown',
            cat='ALL',
            qoljobs_vg=10,
            qoljobs_g=20,
            qoljobs_f=30,
            qoljobs_p=30,
            qoljobs_dnk=5,
            qoljobs_na=5,
            # Add other required fields with sample data
        )
    
    def test_qol_model(self):
        # Test model creation
        self.assertEqual(self.qol_data.name, 'TestTown')
        self.assertEqual(self.qol_data.cat, 'ALL')
        self.assertEqual(self.qol_data.qoljobs_vg, 10)
        self.assertEqual(self.qol_data.qoljobs_g, 20)
