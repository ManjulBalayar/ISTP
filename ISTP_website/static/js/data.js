function renderRadialChart(data, qolDataType) {
    d3.select("#visualization").selectAll("*").remove();

    const width = 500;
    const height = 500;
    const innerRadius = 100;
    const outerRadius = Math.min(width, height) / 2;

    var colorScale = {
        'vg': '#A5D6A7',  // Very Good
        'g': '#C5E1A5',   // Good
        'f': '#FFF59D',   // Fair
        'p': '#FFCC80',   // Poor
        'dnk': '#FFAB91', // Uncertain
        'na': '#BCAAA4'   // None
    };

    const svg = d3.select("#visualization").append("svg")
        .attr("width", width)
        .attr("height", height)
        .append("g")
        .attr("transform", `translate(${width / 2}, ${height / 2})`);

    const x = d3.scaleBand()
        .range([0, 2 * Math.PI])
        .domain(data.map(d => d.group))
        .padding(0.1);

    const y = d3.scaleRadial()
        .range([innerRadius, outerRadius])
        .domain([0, d3.max(data, d => d.value)]);

    svg.append("g")
        .selectAll("path")
        .data(data)
        .enter()
        .append("path")
        .attr("fill", d => colorScale[d.group]) // Apply color based on group directly
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
        .data(data)
        .enter()
        .append("text")
        .attr("text-anchor", "middle")
        .attr("x", d => (y(d.value) + 10) * Math.sin(x(d.group) + x.bandwidth() / 2))
        .attr("y", d => -(y(d.value) + 10) * Math.cos(x(d.group) + x.bandwidth() / 2))
        .text(d => `${d.group} (${d.value})`)
        .style("font-size", "12px")
        .attr("fill", "white");
}

function renderLolipopChart(data, qolDataType) {
    d3.select("#visualization").selectAll("*").remove();

    var margin = {top: 10, right: 30, bottom: 40, left: 100},
        width = 460 - margin.left - margin.right,
        height = 500 - margin.top - margin.bottom;

    var svg = d3.select("#visualization").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    var colorScale = {
        'Very Good': '#A5D6A7',
        'Good': '#C5E1A5',
        'Fair': '#FFF59D',
        'Poor': '#FFCC80',
        'Uncertain': '#FFAB91',
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
        .attr("transform", "translate(0," + height + ")")
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
        .attr("y1", function(d) { return y(d.group); })
        .attr("y2", function(d) { return y(d.group); })
        .attr("stroke", "grey")
        .transition()
        .duration(1000)
        .attr("x1", function(d) { return x(d.value); });

    // Circles with animation
    svg.selectAll("mycircle")
        .data(formattedData)
        .enter()
        .append("circle")
        .attr("cx", x(0))
        .attr("cy", function(d) { return y(d.group); })
        .attr("r", "7")
        .style("fill", function(d) { return colorScale[d.group]; })
        .attr("stroke", "black")
        .transition()
        .duration(1000)
        .attr("cx", function(d) { return x(d.value); });
}

function renderBarChart(data, qolDataType) {
    // Clear any existing SVG
    d3.select("#visualization").selectAll("*").remove();

    // Set the dimensions and margins of the graph
    var margin = {top: 30, right: 30, bottom: 40, left: 50},
        width = 960 - margin.left - margin.right,
        height = 500 - margin.top - margin.bottom;

    // Append the svg object to the body of the page
    var svg = d3.select("#visualization").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
    .append("g")
        .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");

    // Define the new labels
    var labels = {
        'vg': 'Very Good',
        'g': 'Good',
        'f': 'Fair',
        'p': 'Poor',
        'dnk': 'Uncertain',
        'na': 'None'
    };

    // Define the color for each label
    var colorScale = {
        'Very Good': '#A5D6A7', // Softer Green
        'Good': '#C5E1A5', // Softer Light Green
        'Fair': '#FFF59D', // Softer Yellow
        'Poor': '#FFCC80', // Softer Orange
        'Uncertain': '#FFAB91', // Softer Red
        'None': '#BCAAA4' // Softer Dark Red
    };

    // Map data to new labels
    var formattedData = data.map(function(d) {
        var keySuffix = d.group.split('_').pop(); // Extract suffix (e.g., 'vg', 'g')
        var newLabel = labels[keySuffix] || keySuffix; // Map to new label or keep original
        return { group: newLabel, value: d.value };
    });

    // X axis
    var x = d3.scaleBand()
    .range([ 0, width ])
    .domain(formattedData.map(function(d) { return d.group; }))
    .padding(0.2);
    svg.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x))

    // Add Y axis
    var y = d3.scaleLinear()
    .domain([0, 100])
    .range([ height, 0]);
    svg.append("g")
    .call(d3.axisLeft(y));

    // Bars
    svg.selectAll("mybar")
        .data(formattedData)
        .enter()
        .append("rect")
            .attr("x", function(d) { return x(d.group); })
            .attr("y", height)
            .attr("width", x.bandwidth())
            .attr("height", 0)
            .attr("fill", function(d) { return colorScale[d.group]; }) // Assign color based on group
            .transition()
            .duration(800)
            .attr("y", function(d) { return y(d.value); }) // Corrected to 'd.value'
            .attr("height", function(d) { return height - y(d.value); }) // Corrected to 'd.value'
            .delay(function(d, i) { return i * 100; }); // Delay for staggering effect


    // Adding text labels on bars
    svg.selectAll(".text")
    .data(formattedData)
    .enter()
    .append("text")
        .attr("class", "label")
        .attr("x", (function(d) { return x(d.group) + (x.bandwidth() / 2) - 8; }  ))
        .attr("y", function(d) { return y(d.value) - 5; })
        .attr("dy", ".75em")
        .text(function(d) { return d.value; })
        .attr("fill", "#333")
        .style("font-size", "12px")
        .style("text-anchor", "middle");
}

function renderPieChart(data, qolDataType) {
    d3.select("#visualization").selectAll("*").remove();

    var width = 1160, // Increase the width for better spacing
        height = 650,
        margin = 100;
    var radius = Math.min(width, height) / 2 - margin;

    var svg = d3.select("#visualization")
        .append("svg")
        .attr("width", width)
        .attr("height", height)
        .append("g")
        // Center the pie chart within the new SVG dimensions
        .attr("transform", "translate(" + (width / 2 - 50) + "," + height / 2 + ")");

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
        .range(['#A5D6A7', '#C5E1A5', '#FFF59D', '#FFCC80', '#FFAB91', '#BCAAA4']);

    var formattedData = data.map(function(d) {
        var newLabel = labels[d.group.split('_').pop()] || 'Unknown';
        return { group: newLabel, value: d.value };
    });

    var pie = d3.pie().value(function(d) { return d.value; });
    var data_ready = pie(formattedData);

    var arc = d3.arc().innerRadius(0).outerRadius(radius);

    // Append the pie chart slices
    svg.selectAll('mySlices')
        .data(data_ready)
        .enter()
        .append('path')
        .attr('d', arc)
        .attr('fill', function(d) { return colorScale(d.data.group); })
        .attr("stroke", "white")
        .style("stroke-width", "2px")
        .style("opacity", 0.7)
        // Add mouseover event listener
        .on("mouseover", function(event, d) {
            var target = d3.select(this);
            var centroid = arc.centroid(d); // Get the centroid of the slice
            var x = centroid[0] * 0.2; // Calculate the x offset
            var y = centroid[1] * 0.2; // Calculate the y offset
            target.transition()
                .duration(700)
                .attr('transform', 'translate(' + x + ',' + y + ')')
                .style("opacity", 1); // Highlight the slice by increasing opacity
            
            // Append text label for the hovered slice
            svg.append("text")
                .attr("transform", "translate(" + arc.centroid(d) + ")")
                .attr("dy", "0.35em")
                .attr("class", "slice-label") // Use this class to style the text if needed
                .style("text-anchor", "middle")
                .text(function() {
                    return d.data.group + ": " + d.data.value; // Display the label and value
                });
        })
        // Add mouseout event listener
        .on("mouseout", function() {
            d3.select(this).transition()
                .duration(400)
                .attr('transform', 'translate(0,0)')
                .style("opacity", 0.7); // Return to normal opacity
            
            // Remove the text label
            svg.selectAll(".slice-label").remove(); // Remove the label on mouseout
        });
}

$(document).ready(function() {
    $('#data_type').change(function() {
        var selectedType = $(this).val();
        if (selectedType === 'qol') {
            $('#qol_data_type_container').show();
        } else {
            $('#qol_data_type_container').hide();
            $('#qol_data_type').empty().append('<option value="">Select a QOL data type</option>');
        }
    });

    $('#demographic').change(function(){
        var selectedDemographic = $(this).val();
        // Log the selected demographic
        console.log("Selected Demographic: " + selectedDemographic);
        
        $.ajax({
            url: demographicsUrl,
            data: {
                'demographic': selectedDemographic
            },
            dataType: 'json',
            success: function (data) {
                var specificDemographicSelect = $('#specific_demographic');
                specificDemographicSelect.empty();
                specificDemographicSelect.append('<option value=""></option>');
                $.each(data.specific_options, function(index, value) {
                    specificDemographicSelect.append($('<option>', {
                        value: value, // Use value as the option value
                        text: value  // Use value as the option text
                    }));
                });
            }
        });
    });

    // When specific demographic changes
    $('#specific_demographic').change(function(){
        var selectedTown = $('#town').val();
        var selectedDemographic = $(this).val();
        // Log the selected specific demographic
        console.log("Town: " + selectedTown + ", Specific Demographic: " + selectedDemographic);

        var qolDataTypeSelect = $('#qol_data_type');
        qolDataTypeSelect.empty();

        var qolDataTypeSelect = $('#qol_data_type');
        qolDataTypeSelect.empty();
        qolDataTypeSelect.append('<option value="" selected></option>');
        if (selectedDemographic) {
            // Simulated QOL data types
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
        } else {
            qolDataTypeSelect.append($('<option>', {
                value: '',
                text: 'Please select a specific demographic'
            }));
        }

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
            'year': $('#year').val(),  // Add the year to the formData
            'visualization_type': $('#visualization_type').val() // Capture the selected visualization type
        };

        if (formData.data_type === 'qol') {
            formData['qol_data_type'] = $('#qol_data_type').val();
        }

        $.ajax({
            url: query_data,
            method: 'GET',
            data: formData,
            success: function(response) {
                console.log(response);
                $('#qol-results').empty();
                if (response.qol_ratings) {
                    var dataArray = Object.entries(response.qol_ratings).map(function([key, value]) {
                        return { group: key, value: parseFloat(value) };
                    });

                    // Conditional rendering based on the visualization type
                    if (formData['visualization_type'] === 'bar') {
                        renderBarChart(dataArray, formData['qol_data_type']);
                    } else if (formData['visualization_type'] === 'pie') {
                        renderPieChart(dataArray, formData['qol_data_type']);
                    } else if(formData['visualization_type'] === 'lolipop') {
                        renderLolipopChart(dataArray, formData['qol_data_type'])
                    } else if(formData['visualization_type'] === 'radial') {
                        renderRadialChart(dataArray, formData['qol_data_type'])
                    } 
                    // Smoothly scroll to the visualization section
                    $('html, body').animate({
                        scrollTop: $("#visualization").offset().top
                    }, 80); // Adjust the scroll speed if necessary
                } else if (response.error) {
                    $('#qol-results').append(`<p>Error: ${response.error}</p>`);
                }
            },
            error: function(xhr, status, error) {
                console.error("Error: " + error);
            }
        });
    });
});
