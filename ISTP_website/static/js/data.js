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

function renderBarChart(data, qolDataType) {
    d3.select("#barChartContainer").selectAll("*").remove();

    var container = d3.select("#barChartContainer");
    const width = parseInt(container.style("width")) - 100;  // Adjusting for margins
    const height = parseInt(container.style("height")) - 60;  // Adjusting for margins

    var svg = container.append("svg")
        .attr("width", width + 100)  // Add back margins
        .attr("height", height + 60)
        .append("g")
        .attr("transform", "translate(50, 30)");  // Apply some margins for axis

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

    var formattedData = data.map(function(d) {
        var keySuffix = d.group.split('_').pop();
        var newLabel = labels[keySuffix] || keySuffix;
        return { group: newLabel, value: d.value };
    });

    var x = d3.scaleBand()
        .range([0, width])
        .domain(formattedData.map(function(d) { return d.group; }))
        .padding(0.2);

    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));

    var y = d3.scaleLinear()
        .domain([0, d3.max(formattedData, d => d.value)])
        .range([height, 0]);

    svg.append("g")
        .call(d3.axisLeft(y));

    // Bars with animation
    svg.selectAll("mybar")
        .data(formattedData)
        .enter()
        .append("rect")
            .attr("x", d => x(d.group))
            .attr("y", d => height)  // Start bars at the bottom of the axis
            .attr("width", x.bandwidth())
            .attr("height", 0)  // Initially set height to 0
            .attr("fill", d => colorScale[d.group])
            .transition()
            .duration(800)
            .attr("y", d => y(d.value))  // End position of the bar
            .attr("height", d => height - y(d.value))  // Proper height of the bar
            .delay((d, i) => i * 100);  // Stagger the animation

    // Adding text labels on bars
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
    $(document).ready(function() {
        // When 'Select Type of Data' changes
        $('#data_type').change(function() {
            var selectedType = $(this).val();
            if (selectedType === 'qol') {
                // Show 'Select QOL Data Type' and populate it immediately
                $('#qol_data_type_container').show();
                populateQOLDataType();  // Populate the QOL Data Type options
            } else {
                $('#qol_data_type_container').hide();
                $('#qol_data_type').empty().append('<option value="">Select a QOL data type</option>');
            }
        });
    
        // Populate QOL Data Type dropdown
        function populateQOLDataType() {
            var qolDataTypeSelect = $('#qol_data_type');
            qolDataTypeSelect.empty();
            qolDataTypeSelect.append('<option value="" selected> </option>');
            
            // Predefined QOL options
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
    
            // Dynamically add QOL options to the dropdown
            $.each(qolOptions, function(key, label) {
                qolDataTypeSelect.append($('<option>', {
                    value: key,
                    text: label
                }));
            });
        }
    
        // No changes to demographics functionality, this stays the same
        $('#demographic').change(function() {
            var selectedDemographic = $(this).val();
            // Fetch specific demographics based on the selected demographic
            $.ajax({
                url: demographicsUrl,
                data: { 'demographic': selectedDemographic },
                dataType: 'json',
                success: function(data) {
                    var specificDemographicSelect = $('#specific_demographic');
                    specificDemographicSelect.empty();
                    specificDemographicSelect.append('<option value=""></option>');
                    $.each(data.specific_options, function(index, value) {
                        specificDemographicSelect.append($('<option>', {
                            value: value,
                            text: value
                        }));
                    });
                }
            });
        });
    });    

    // When QOL data type changes
    $('#qol_data_type').change(function(){
        var selectedQOLDataType = $(this).val();
        // Log the selected QOL data type
        console.log("Selected QOL Data Type: " + selectedQOLDataType);
    });

    $('#selection-form').on('submit', function(event) {
        event.preventDefault();
        var formData = {
            'town': $('#town').val(),
            'demographic': $('#demographic').val(),
            'specific_demographic': $('#specific_demographic').val(),
            'data_type': $('#data_type').val(),
            'year': $('#year').val(),
            'visualization_type': $('#visualization_type').val()
        };
    
        if (formData.data_type === 'qol') {
            formData['qol_data_type'] = $('#qol_data_type').val();
        }
    
        // Smoothly scroll to the visualization section first
        $('html, body').animate({
            scrollTop: $("#visualization").offset().top
        }, 800, function() {
            // Prepare visualization area after scroll
            prepareVisualizationArea();
            
            // Fetch data and render charts after scrolling
            $.ajax({
                url: query_data,
                method: 'GET',
                data: formData,
                success: function(response) {
                    if (response.qol_ratings) {
                        var dataArray = Object.entries(response.qol_ratings).map(([key, value]) => {
                            return { group: key, value: parseFloat(value) };
                        });
                        // Render all charts after the scroll has finished
                        renderBarChart(dataArray, formData['qol_data_type']);
                        renderPieChart(dataArray, formData['qol_data_type']);
                        renderLolipopChart(dataArray, formData['qol_data_type']);
                        renderRadialChart(dataArray, formData['qol_data_type']);
                        // Make visualization area visible
                        $('#visualization').css('visibility', 'visible');
                    } else if (response.error) {
                        $('#visualization').append(`<p>Error: ${response.error}</p>`);
                    }
                },
                error: function(xhr, status, error) {
                    console.error("Error: " + error);
                }
            });
        });
    });
    
    function prepareVisualizationArea() {
        // Clear previous charts
        $('#visualization').empty();
    
        // Create containers for each chart type
        $('<div id="barChartContainer" class="visualization-container"></div>').appendTo('#visualization');
        $('<div id="pieChartContainer" class="visualization-container"></div>').appendTo('#visualization');
        $('<div id="lolipopChartContainer" class="visualization-container"></div>').appendTo('#visualization');
        $('<div id="radialChartContainer" class="visualization-container"></div>').appendTo('#visualization');
    }
        
});
