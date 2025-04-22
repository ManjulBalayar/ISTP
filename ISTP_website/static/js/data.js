function renderRadialChart(data, qolDataType) {
    d3.select("#radialChartContainer").selectAll("*").remove();

    var container = d3.select("#radialChartContainer");
    const width = parseInt(container.style("width"));
    const height = parseInt(container.style("height"));
    const innerRadius = width / 5;  // Example proportion, adjust as needed
    const outerRadius = Math.min(width, height) / 2 - 20; // Leave some margin

    var colorScale = {
        'Very Good': '#A5D6A7',
        'Good': '#C5E1A5',
        'Fair': '#FFF59D',
        'Poor': '#FFAB91',
        'Uncertain': '#FFCC80',
        'None': '#BCAAA4'
    };

    var labels = {
        'vg': 'Very Good',
        'g': 'Good',
        'f': 'Fair',
        'p': 'Poor',
        'dnk': 'Uncertain',
        'na': 'None'
    };

    var formattedData = data.map(function(d) {
        var keySuffix = d.group.split('_').pop();
        var newLabel = labels[keySuffix] || keySuffix;
        return { group: newLabel, value: d.value };
    });

    const svg = container.append("svg")
        .attr("width", width)
        .attr("height", height)
        .append("g")
        .attr("transform", `translate(${width / 2}, ${height / 2})`);

    const x = d3.scaleBand()
        .range([0, 2 * Math.PI])
        .domain(formattedData.map(d => d.group))
        .padding(0.1);

    const y = d3.scaleRadial()
        .range([innerRadius, outerRadius])
        .domain([0, d3.max(formattedData, d => d.value)]);

    svg.append("g")
        .selectAll("path")
        .data(formattedData)
        .enter()
        .append("path")
        .attr("fill", d => colorScale[d.group])
        .attr("d", d3.arc()
            .innerRadius(innerRadius)
            .outerRadius(d => y(d.value))
            .startAngle(d => x(d.group))
            .endAngle(d => x(d.group) + x.bandwidth())
            .padAngle(0.01)
            .padRadius(innerRadius));

    // Adding labels (optional)
    svg.append("g")
        .selectAll("text")
        .data(formattedData)
        .enter()
        .append("text")
        .attr("text-anchor", "middle")
        .attr("x", d => (y(d.value) + 10) * Math.sin(x(d.group) + x.bandwidth() / 2))
        .attr("y", d => -(y(d.value) + 10) * Math.cos(x(d.group) + x.bandwidth() / 2))
        .text(d => `${d.group} (${d.value})`)
        .style("font-size", "12px")
        .attr("fill", "black");
}

function renderLolipopChart(data, qolDataType) {
    d3.select("#lolipopChartContainer").selectAll("*").remove();

    var container = d3.select("#lolipopChartContainer");
    const containerWidth = parseInt(container.style("width"));
    const containerHeight = parseInt(container.style("height"));

    // Increase bottom margin to provide more space for x-axis labels
    var margin = {top: 10, right: 30, bottom: 60, left: 100},
        width = containerWidth - margin.left - margin.right,
        height = containerHeight - margin.top - margin.bottom;

    var svg = container.append("svg")
        .attr("width", containerWidth)
        .attr("height", containerHeight)
        .append("g")
        .attr("transform", `translate(${margin.left}, ${margin.top})`);

    var colorScale = {
        'Very Good': '#A5D6A7',
        'Good': '#C5E1A5',
        'Fair': '#FFF59D',
        'Poor': '#FFAB91',
        'Uncertain': '#FFCC80',
        'None': '#BCAAA4'
    };

    var labels = {
        'vg': 'Very Good',
        'g': 'Good',
        'f': 'Fair',
        'p': 'Poor',
        'dnk': 'Uncertain',
        'na': 'None'
    };

    var formattedData = data.map(function(d) {
        var keySuffix = d.group.split('_').pop();
        var newLabel = labels[keySuffix] || keySuffix;
        return { group: newLabel, value: d.value };
    });

    formattedData.sort(function(a, b) {
        return b.value - a.value;
    });

    var x = d3.scaleLinear()
        .domain([0, d3.max(formattedData, function(d) { return d.value; })])
        .range([0, width]);
    svg.append("g")
        .attr("transform", `translate(0, ${height})`)
        .call(d3.axisBottom(x));

    var y = d3.scaleBand()
        .range([0, height])
        .domain(formattedData.map(function(d) { return d.group; }))
        .padding(1);
    svg.append("g")
        .call(d3.axisLeft(y));

    // Lines with animation
    svg.selectAll("myline")
        .data(formattedData)
        .enter()
        .append("line")
        .attr("x1", x(0))
        .attr("x2", x(0))
        .attr("y1", d => y(d.group))
        .attr("y2", d => y(d.group))
        .attr("stroke", "grey")
        .transition()
        .duration(1000)
        .attr("x1", d => x(d.value));

    // Circles with animation
    svg.selectAll("mycircle")
        .data(formattedData)
        .enter()
        .append("circle")
        .attr("cx", x(0))
        .attr("cy", d => y(d.group))
        .attr("r", "7")
        .style("fill", d => colorScale[d.group])
        .attr("stroke", "black")
        .transition()
        .duration(1000)
        .attr("cx", d => x(d.value));
}

function renderPieChart(data, qolDataType) {
    d3.select("#pieChartContainer").selectAll("*").remove();

    var container = d3.select("#pieChartContainer");
    const width = parseInt(container.style("width"));
    const height = parseInt(container.style("height"));
    const radius = Math.min(width, height) / 2 - 50; // Adjust radius for margins

    var svg = container.append("svg")
        .attr("width", width)
        .attr("height", height)
        .append("g")
        .attr("transform", `translate(${width / 2}, ${height / 2})`);

    var labels = {
        'vg': 'Very Good',
        'g': 'Good',
        'f': 'Fair',
        'p': 'Poor',
        'dnk': 'Uncertain',
        'na': 'None'
    };

    var colorScale = d3.scaleOrdinal()
        .domain(Object.values(labels))
        .range(['#A5D6A7', '#C5E1A5', '#FFF59D', '#FFAB91', '#FFCC80', '#BCAAA4']);

    var formattedData = data.map(function(d) {
        var newLabel = labels[d.group.split('_').pop()] || 'Unknown';
        return { group: newLabel, value: d.value };
    });

    var pie = d3.pie().value(function(d) { return d.value; });
    var data_ready = pie(formattedData);

    var arc = d3.arc().innerRadius(0).outerRadius(radius);
    var arcHover = d3.arc().innerRadius(0).outerRadius(radius + 20); // Hover state

    // Append paths
    var paths = svg.selectAll('path')
        .data(data_ready)
        .enter()
        .append('path')
        .attr('fill', d => colorScale(d.data.group))
        .attr("stroke", "white")
        .style("stroke-width", "2px")
        .style("opacity", 0.7)
        .attr('d', arc);

    // Append the text label after paths to ensure it's on top
    var label = svg.append("text")
        .attr("dy", "0.35em")
        .attr("class", "slice-label")
        .style("text-anchor", "middle")
        .style("opacity", 0)  // Initially hidden
        .style("font-weight", "bold")  // Make text bold
        .style("fill", "black")  // Set a high contrast color
        .style("pointer-events", "none");  // Make text non-interactive

    // Interaction effects
    paths.on("mouseover", function(event, d) {
        d3.select(this)
            .transition()
            .duration(300)
            .attr('d', arcHover)
            .style("opacity", 1);

        // Update text label positions and text based on current slice
        label.attr("transform", `translate(${arcHover.centroid(d)})`)
            .text(`${d.data.group}: ${d.data.value}`)
            .style("opacity", 1);  // Make visible
    })
    .on("mouseout", function(d) {
        d3.select(this)
            .transition()
            .duration(300)
            .attr('d', arc)
            .style("opacity", 0.7);

        // Hide label
        label.style("opacity", 0);
    });
}

$(document).ready(function() {
    // When 'Select Type of Data' changes
    $('#data_type').change(function() {
        var selectedType = $(this).val();
        if (selectedType === 'qol') {
            $('#qol_data_type_container').show();
            populateQOLDataType();
        } else {
            $('#qol_data_type_container').hide();
            $('#qol_data_type').empty().append('<option value=""> </option>');
        }
    });

    // Populate QOL Data Type dropdown
    function populateQOLDataType() {
        var qolDataTypeSelect = $('#qol_data_type');
        qolDataTypeSelect.empty();
        qolDataTypeSelect.append('<option value="" selected></option>');
        
        var qolOptions = {
            'Jobs': 'Jobs',
            'Medical': 'Medical',
            'shop': 'Shopping Options',
            'k12': 'Public School',
            'Housing': 'Housing',
            'Childcare': 'Childcare',
            'Seniorcare': 'Seniorcare',
            'Youth': 'Youth Programs',
            'commsrvall': 'Community Services Overall',
            'recrentr': 'Recreation and Entertainment',
            'Police': 'Police',
            'Fire': 'Fire',
            'ems': 'Emergency Medical Services',
            'Streets': 'Condition of Streets',
            'Parks': 'Condition of Parks',
            'Garbage': 'Garbage Collection',
            'Water': 'Water',
            'govtsrvall': 'Government Services Overall'
        };

        $.each(qolOptions, function(key, label) {
            qolDataTypeSelect.append($('<option>', {
                value: key,
                text: label
            }));
        });
    }

    // New autocomplete functionality for town selection
    var townInput = $('#town-search');
    var townSelect = $('#town');
    var townOptions = townSelect.find('option').map(function() {
        return { value: $(this).val(), text: $(this).text() };
    }).get();

    townInput.autocomplete({
        source: function(request, response) {
            var term = request.term.toLowerCase();
            var matches = townOptions.filter(function(option) {
                return option.text.toLowerCase().indexOf(term) === 0;
            });
            response(matches);
        },
        minLength: 0,
        select: function(event, ui) {
            townInput.val(ui.item.text);
            townSelect.val(ui.item.value);
            return false;
        }
    }).focus(function() {
        $(this).autocomplete("search", "");
    });

    townInput.on('input', function() {
        var value = $(this).val();
        var option = townOptions.find(function(option) {
            return option.text.toLowerCase() === value.toLowerCase();
        });
        townSelect.val(option ? option.value : '');
    });

    // Handle the 'Visualize' button press to generate the visualizations
    $('#selection-form').on('submit', function(event) {
        event.preventDefault();

        // Clear any existing error messages
        $('.error-message').remove();

        var selectedDemographic = $('#demographic').val();
        var selectedTown = $('#town').val();
        var selectedYear = $('#year').val();
        var selectedQOLType = $('#qol_data_type').val();
        var dataType = $('#data_type').val();

        // Validate form inputs
        var errors = [];

        if (!selectedYear) {
            errors.push("Please select a year.");
        }

        if (!selectedTown) {
            errors.push("Please select a town.");
        }

        if (!dataType) {
            errors.push("Please select a type of data.");
        }

        if (dataType === 'qol' && !selectedQOLType) {
            errors.push("Please select a QOL data type.");
        }

        if (!selectedDemographic) {
            errors.push("Please select a demographic.");
        }

        // If there are errors, display them and stop the submission
        if (errors.length > 0) {
            var errorHtml = '<div class="error-message" style="color: red; margin-bottom: 15px;"><ul>';
            errors.forEach(function(error) {
                errorHtml += '<li>' + error + '</li>';
            });
            errorHtml += '</ul></div>';
            $(this).prepend(errorHtml);
            return;
        }

        // If all validations pass, proceed with data fetching and visualization
        $.ajax({
            url: demographicsUrl,
            data: { 'demographic': selectedDemographic },
            dataType: 'json',
            success: function(data) {
                prepareVisualizationArea();

                var chartsToRender = data.specific_options.length;
                var chartsRendered = 0;

                // For each specific demographic, generate a separate bar chart
                $.each(data.specific_options, function(index, specificDemographic) {
                    $.ajax({
                        url: query_data,
                        method: 'GET',
                        data: {
                            'town': selectedTown,
                            'demographic': selectedDemographic,
                            'specific_demographic': specificDemographic,
                            'data_type': dataType,
                            'qol_data_type': selectedQOLType,
                            'year': selectedYear
                        },
                        success: function(response) {
                            if (response.qol_ratings) {
                                var dataArray = Object.entries(response.qol_ratings).map(([key, value]) => {
                                    return { group: key, value: parseFloat(value) };
                                });
                
                                var containerId = 'chart-' + specificDemographic.replace(/\s+/g, '-');
                                var container = $('<div id="' + containerId + '" class="visualization-container"></div>');
                                
                                var demographicLabel = getHumanReadableLabel(specificDemographic);
                                
                                $('#visualization').append(container);
                                
                                // Pass the additional parameters here to renderBarChart
                                renderBarChart(dataArray, containerId, demographicLabel, selectedYear, selectedTown, dataType, selectedQOLType);
                                $('#visualization').css('visibility', 'visible');
                
                                chartsRendered++;
                
                                if (chartsRendered === chartsToRender) {
                                    scrollToVisualization();
                                }
                            } else if (response.error) {
                                $('#visualization').append(`<p class="error-message" style="color: red;">Error: ${response.error}</p>`);
                                chartsRendered++;
                            }
                        },
                        error: function(xhr, status, error) {
                            console.error("Error: " + error);
                            $('#visualization').append(`<p class="error-message" style="color: red;">Error: Unable to fetch data. Please try again later.</p>`);
                            chartsRendered++;
                        }
                    });
                });
                
            },
            error: function(xhr, status, error) {
                console.error("Error fetching demographics: " + error);
                $('#visualization').append(`<p class="error-message" style="color: red;">Error: Unable to fetch demographic data. Please try again later.</p>`);
            }
        });
    });

    // Handle the reset button click
    $('#reset-form').on('click', function() {
        $('#selection-form select').val('');
        $('#qol_data_type_container').hide();
        $('#qol_data_type').empty().append('<option value=""> </option>');
        townInput.val('');  // Clear the town search input
    });

    // Clear previous charts and prepare the visualization area
    function prepareVisualizationArea() {
        $('#visualization').empty();
    }

    // Function to scroll to the visualization area
    function scrollToVisualization() {
        // Wait for a short moment to ensure all charts are rendered
        setTimeout(function() {
            var visualizationTop = $("#visualization").offset().top;
            var windowHeight = $(window).height();
            var scrollTo = visualizationTop - (windowHeight * 0.1); // Scroll to 10% from the top of the window

            $('html, body').animate({
                scrollTop: scrollTo
            }, 300); // Faster scroll duration (300ms instead of 500ms)
        }, 100); // Short delay to ensure charts are rendered
    }

    // Render bar chart function
    function renderBarChart(dataArray, containerId, demographicLabel, selectedYear, selectedTown, dataType, selectedQOLType) {
        d3.select("#" + containerId).selectAll("*").remove();

        var container = d3.select("#" + containerId);
        const margin = { top: 130, right: 50, bottom: 50, left: 50 };
        const width = container.node().getBoundingClientRect().width - margin.left - margin.right;
        const height = 400 - margin.top - margin.bottom;
    
        // Define qolOptions for human-readable labels
        var qolOptions = {
            'Jobs': 'Jobs',
            'Medical': 'Medical',
            'shop': 'Shopping Options',
            'k12': 'Public School',
            'Housing': 'Housing',
            'Childcare': 'Childcare',
            'Seniorcare': 'Seniorcare',
            'Youth': 'Youth Programs',
            'commsrvall': 'Community Services Overall',
            'recrentr': 'Recreation and Entertainment',
            'Police': 'Police',
            'Fire': 'Fire',
            'ems': 'Emergency Medical Services',
            'Streets': 'Condition of Streets',
            'Parks': 'Condition of Parks',
            'Garbage': 'Garbage Collection',
            'Water': 'Water',
            'govtsrvall': 'Government Services Overall'
        };
    
        // Get the human-readable QOL data type
        var qolLabel = qolOptions[selectedQOLType] || selectedQOLType; // Default to original if not found in qolOptions
    
        // Append an SVG element for the chart with margins
        var svg = container.append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")"); // Adjusted translate for more space
    
        var labels = {
            'vg': 'Very Good',
            'g': 'Good',
            'f': 'Fair',
            'p': 'Poor',
            'dnk': 'Uncertain',
            'na': 'None'
        };
    
        var colorScale = {
            'Very Good': '#A5D6A7',
            'Good': '#C5E1A5',
            'Fair': '#FFF59D',
            'Poor': '#FFAB91',
            'Uncertain': '#FFCC80',
            'None': '#BCAAA4'
        };
    
        // Format the data
        var formattedData = dataArray.map(function(d) {
            var keySuffix = d.group.split('_').pop();
            var newLabel = labels[keySuffix] || keySuffix;
            return { group: newLabel, value: d.value };
        });
    
        // X axis
        var x = d3.scaleBand()
            .range([0, width])
            .domain(formattedData.map(function(d) { return d.group; }))
            .padding(0.2);
    
        svg.append("g")
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(x));
    
        // Y axis (set to a fixed range from 0 to 100)
        var y = d3.scaleLinear()
            .domain([0, 100]) // Fixed range from 0 to 100
            .range([height, 0]);
    
        svg.append("g")
            .call(d3.axisLeft(y));
    
        // Bars
        svg.selectAll("mybar")
            .data(formattedData)
            .enter()
            .append("rect")
            .attr("x", d => x(d.group))
            .attr("y", d => y(0))
            .attr("width", x.bandwidth())
            .attr("height", 0)
            .attr("fill", d => colorScale[d.group])
            .transition()
            .duration(800)
            .attr("y", d => y(d.value))
            .attr("height", d => height - y(d.value))
            .delay((d, i) => i * 100);
    
        // Add labels to bars
        svg.selectAll(".text")
            .data(formattedData)
            .enter()
            .append("text")
            .attr("class", "label")
            .attr("x", d => x(d.group) + x.bandwidth() / 2)
            .attr("y", d => y(d.value) - 5)
            .attr("dy", ".75em")
            .text(d => d.value)
            .attr("fill", "#333")
            .style("font-size", "12px")
            .style("text-anchor", "middle");
    
        // Add demographic label to the regular labels in the label container
        container.append("div")
            .attr("class", "label-container")
            .html(`
                <strong>Demographic:</strong> ${demographicLabel}<br>
                <strong>Year:</strong> ${selectedYear}<br>
                <strong>Town:</strong> ${selectedTown}<br>
                <strong>Data Type:</strong> ${dataType === 'qol' ? 'Quality of Life' : 'Other'}<br>
                ${dataType === 'qol' ? `<strong>QOL Data Type:</strong> ${qolLabel}<br>` : ''}
            `);
        
        container.append("button")
            .attr("class", "download-button")
            .attr("title", "Download chart")
            .html('<svg class="download-icon" viewBox="0 0 24 24"><path d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"/></svg>')
            .on("click", function() {
                downloadChartAsImage(containerId, demographicLabel, selectedYear, selectedTown);
            });
    }   

    function downloadChartAsImage(containerId, demographicLabel, selectedYear, selectedTown) {
        var container = document.getElementById(containerId);
        
        html2canvas(container).then(function(canvas) {
            // Create a temporary anchor element
            var link = document.createElement('a');
            link.download = `Chart_${demographicLabel}_${selectedYear}_${selectedTown}.png`.replace(/\s+/g, '_');
            link.href = canvas.toDataURL("image/png");
            link.click();
        });
    }
           
    // Function to get human-readable label for specific demographics
    function getHumanReadableLabel(specificDemographic) {
        var labels = {
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
        };
        return labels[specificDemographic] || specificDemographic;
    }
});

//so as you know from my code, it creates different graphs based on your dropdown selections. These charts are being generated using the library D3js. 
//Is it possible to make like a small copy button that basically copies the generated graph image with the labels?