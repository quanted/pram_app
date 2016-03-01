// Placeholder object for User changed values
var dragVal = {};

//import data from a json file and run drawSliders function onPageLoad
d3.json("/static/json/baseline.json", function (data) {
    dragVal = data;
    data.Services.forEach(drawSliders);  // Call drawSliders() after parsing JSON, passing in "each" element
});


//draw sliders function
function drawSliders(data, index) {
    //append an svg to cirSlide div

    //set scale for slider. domain is input min max. range is slider translated min max (same)
var x = d3.scale.linear()
    .domain((function () {
            if (data.ServiceName == "Capital Investment") { return [56, 62]; }
            if (data.ServiceName == "Consumption") { return [47, 54]; }
            if (data.ServiceName == "Employment") { return [33, 73]; }
            if (data.ServiceName == "Finance") { return [31, 62]; }
            if (data.ServiceName == "Innovation") { return [26, 65]; }
            if (data.ServiceName == "Production") { return [45, 52]; }
            if (data.ServiceName == "Re-Distribution") { return [24, 69]; }
            if (data.ServiceName == "Air Quality") { return [10, 90]; }
            if (data.ServiceName == "Food, Fiber And Fuel Provisioning") { return [33, 48]; }
            if (data.ServiceName == "Greenspace") { return [36, 62]; }
            if (data.ServiceName == "Water Quality") { return [16, 88]; }
            if (data.ServiceName == "Water Quantity") { return [22, 73]; }
            if (data.ServiceName == "Activism") { return [26, 74]; }
            if (data.ServiceName == "Communication") { return [33, 69]; }
            if (data.ServiceName == "Community And Faith-Based Initiatives") { return [12, 90]; }
            if (data.ServiceName == "Education") { return [33, 56]; }
            if (data.ServiceName == "Emergency Preparedness") { return [12, 90]; }
            if (data.ServiceName == "Family Services") { return [43, 73]; }
            if (data.ServiceName == "Healthcare") { return [30, 62]; }
            if (data.ServiceName == "Justice") { return [31, 72]; }
            if (data.ServiceName == "Labor") { return [37, 53]; }
            if (data.ServiceName == "Public Works") { return [34, 66]; }
        })()
    )
    .range([1, 99])
    //make scale *always* abide by range
    .clamp(true);

    var svgslide = d3.select("#cirSlide").append("svg")
        .attr("width", 180)
        .attr("height", 40)


    //append an empty group element to the svg for x axis slider bar
    svgslide.append("g")
        //set g element with attribute "x axis" (html attribute used for css styling)
        .attr("class", "x axis")
        //move g element over 25px to create margin
        .attr("transform", "translate(" + 10 + "," + 25 + ")")
        // introduce x-axis and give scale and no ticks
        .call(d3.svg.axis()
            .scale(x)
            .tickSize(0)
            .tickPadding(0))
        //select the axis domain (min max range)
        .select(".domain")
        //set axis with attribute halo to use as slider bar
        .attr("class", "halo");


    //append service name text to svg variables
    var name = svgslide.append("text")
        .text(function () {
            return data.ServiceName
        })
        .attr('y', 12)
        .attr('x', 10);

    //define brush attributes
    var brush = d3.svg.brush()
        //set scale of brush to match d3 calculated scale
        .x(x)
        //set the input value using imported data Score value
        .extent([data.Score * 100, data.Score * 100])
        //set listener where on mousemove = function brushed
        .on("brush", brushed);

    //create a slider variable and append new g element
    var slider = svgslide.append("g")
        //give new g element class "slider"
        .attr("class", "slider")
        //call the brush variable attributes
        .call(brush)
        .attr("transform", "translate(" + 10 + "," + 0 + ")");

    //set the vertical range of slider background for selection/drag
    slider.select(".background")
        .attr("height", 100);

    //append handle to slider element
    var handle = slider.append("g")
        .attr("class", "handle"+index);

    //append circle to the slider handle
    handle.append("circle")
    //give the circle element class "handle"
    .attr("class", "handle")
    .attr("transform", "translate(0," + 25 + ")")
    .attr("r", 10)
    .attr("fill", (function () {
        if (data.ServiceType == "Economic") { return "#b86361"; }
        if (data.ServiceType == "Ecosystem") { return "#61b88e"; }
        if (data.ServiceType == "Social") { return "#618bb8"; }
    }))

    //append text to the handle
    handle.append('text')
        .attr("class", "cirTex"+index)
        //assign text using data score and convert to whole number
        .text(data.Score * 100)
        .attr("transform", "translate(" + (-8) + " ," + 29 + ")");

    //for slider variable, call brush variable's "brushed" event property (mousemove)
    slider
        .call(brush.event)
        .attr("transform", "translate(" + 10 + "," + 0 + ")")

    //create brushed function
    function brushed() {
        //create variable based on brush extent (x value)
        var value = brush.extent()[0];
        //if the brush mousemove isn't a programmatic event... 
        if (d3.event.sourceEvent) {
            //...select the handle text
            handle.select('text');
            //set new value. constrain to domain value for x axis.
            //set value using mouse position relative to a specified container (0)
            value = x.invert(d3.mouse(this)[0]);
            //set brush extent to only use value (not a broad range)
            brush.extent([value, value]);
        }

        //move the starting handle to the value on x axis
        handle.attr("transform", "translate(" + x(value) + ",0)");
        //round text value down
        handle.select("text").text(Math.floor(value));
        
        dragVal.Services[index].Score = value;       
    }
}


function useServiceValues() {
    //$.getJSON('api/HWBI?CapitalInvestmentScore=58.9&ConsumptionScore=51.6&EmploymentScore=52.3&FinanceScore=44.0&InnovationScore=43.24&ProductionScore=50.44&ReDistributionScore=47.2&AirQualityScore=0.9&FoodFoberAndFuleProvisioningScore=44.44&GreenspaceScore=42.6&WaterQualityScore=67.4&WaterQuantityScore=37.9&ActivismScore=48.9&CommunicationScore=43.4&CommunityAndFaithBasedInitiativesScore=15.81&EducationScore=45.0&EmergencyPreparednessScore=52.6&FamilyServicesScore=50.0&HealthcareScore=48.7&JusticeScore=42.76&LaborScore=40.82&PublicWorksScore=41.84&ConnectionToNatureDomainWeight=1.0&CulturalFulfillmentDomainWeight=1.0&EducationDomainWeight=1.0&HealthDomainWeight=1.0&LeisureTimeDomainWeight=1.0&LivingStandardsDomainWeight=1.0&SafetyAndSecurityDomainWeight=1.0&SocialCohesionDomainWeight=1.0', function (data) {
    $.getJSON('api/HWBI?CapitalInvestmentScore=' + dragVal.Services[0].Score + '&ConsumptionScore=' + dragVal.Services[1].Score + '&EmploymentScore=' + dragVal.Services[2].Score + '&FinanceScore=' + dragVal.Services[3].Score + '&InnovationScore=' + dragVal.Services[4].Score + '&ProductionScore=' + dragVal.Services[5].Score + '&ReDistributionScore=' + dragVal.Services[6].Score + '&AirQualityScore=' + dragVal.Services[7].Score + '&FoodFoberAndFuleProvisioningScore=' + dragVal.Services[8].Score + '&GreenspaceScore=' + dragVal.Services[9].Score + '&WaterQualityScore=' + dragVal.Services[10].Score + '&WaterQuantityScore=' + dragVal.Services[11].Score + '&ActivismScore=' + dragVal.Services[12].Score + '&CommunicationScore=' + dragVal.Services[13].Score + '&CommunityAndFaithBasedInitiativesScore=' + dragVal.Services[14].Score + '&EducationScore=' + dragVal.Services[15].Score + '&EmergencyPreparednessScore=' + dragVal.Services[16].Score + '&FamilyServicesScore=' + dragVal.Services[17].Score + '&HealthcareScore=' + dragVal.Services[18].Score + '&JusticeScore=' + dragVal.Services[19].Score + '&LaborScore=' + dragVal.Services[20].Score + '&PublicWorksScore=' + dragVal.Services[21].Score + '&ConnectionToNatureDomainWeight=' + dragVal.Domains[0].Weight + '&CulturalFulfillmentDomainWeight=' + dragVal.Domains[1].Weight + '&EducationDomainWeight=' + dragVal.Domains[2].Weight + '&HealthDomainWeight=' + dragVal.Domains[3].Weight + '&LeisureTimeDomainWeight=' + dragVal.Domains[4].Weight + '&LivingStandardsDomainWeight=' + dragVal.Domains[5].Weight + '&SafetyAndSecurityDomainWeight=' + dragVal.Domains[6].Weight + '&SocialCohesionDomainWeight=' + dragVal.Domains[7].Weight, function (data) {
        updateDomainScores(data.Domains);
        updateRIVWeights(dragVal.Domains);
    });
}

//function to update RIV domain weight values
function updateRIVWeights(domains) {
    $('#ConnectionToNatureDomainWeight').val(domains[0].Weight);
    $('#CulturalFulfillmentDomainWeight').val(domains[1].Weight);
    $('#EducationDomainWeight').val(domains[2].Weight);
    $('#HealthDomainWeight').val(domains[3].Weight);
    $('#LeisureTimeDomainWeight').val(domains[4].Weight);
    $('#LivingStandardsDomainWeight').val(domains[5].Weight);
    $('#SafetyAndSecurityDomainWeight').val(domains[6].Weight);
    $('#SocialCohesionDomainWeight').val(domains[7].Weight);
}


//function to update services on county selection
function updateServiceScores(servicesScores) {
    servicesScores.forEach(updateSliders);
};


//update sliders chart function
function updateSliders(data, index) {

    //define brush attributes
    var brush = d3.svg.brush()
        //set scale of brush to match d3 calculated scale
        .x(x)
        //set the input value using imported data Score value
        .extent([data.Score * 100, data.Score * 100])
        //set listener where on mousemove = function brushed
        .on("brush", brushed);



    //select handle to slider element
    var handle = d3.select("g.handle" + index)


    //select circle to the slider handle
    d3.select("handle.circle")
        //give the circle element class "handle"
        .attr("class", "handle")
        .attr("transform", "translate(0," + 25 + ")")
        .attr("r", 10)
        .attr("fill", (function () {
            if (data.ServiceType == "Economic") { return "#b86361"; }
            if (data.ServiceType == "Ecosystem") { return "#61b88e"; }
            if (data.ServiceType == "Social") { return "#618bb8"; }
        }))

    //select text to the handle
    d3.select("text.cirTex" + [index])
        //assign text using data score and convert to whole number
        .text(data.Score * 100)
        .attr("transform", "translate(" + (-8) + " ," + 29 + ")");

    //for slider variable, call brush variable's "brushed" event property (mousemove)
    d3.select("g.slider")
        .call(brush.event)
        .attr("transform", "translate(" + 10 + "," + 0 + ")")

    //create brushed function
    function brushed() {
        //create variable based on brush extent (x value)
        var value = brush.extent()[0];
        //if the brush mousemove isn't a programmatic event... 
        if (d3.event.sourceEvent) {
            //...select the handle text
            handle.select("text.cirTex" + [index]);
            //set new value. constrain to domain value for x axis.
            //set value using mouse position relative to a specified container (0)
            value = x.invert(d3.mouse(this)[0]);
            //set brush extent to only use value (not a broad range)
            brush.extent([value, value]);
         }

    //move the starting handle to the value on x axis
    handle.attr("transform", "translate(" + x(value) + ",0)")
        .transition()
        .duration(3000)
        //round text value down
    handle.select("text.cirTex"+[index]).text(Math.floor(value))
    }
}