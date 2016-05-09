// Placeholder object for User changed values
var dragVal = {};

//import data from a json file and run drawSliders function onPageLoad
d3.json("/static/json/baseline.json", function (data) {
    dragVal = data;
    data.results.services.forEach(drawSliders);  // Call drawSliders() after parsing JSON, passing in "each" element
});


//draw sliders function
function drawSliders(data, index) {
    //append an svg to cirSlide div

    //set scale for slider. domain is input min max. range is slider translated min max (same)
var x = d3.scale.linear()
    .domain((function () {
            if (data.ServiceName == "Capital Investment") { return [56.31683197, 61.75389692]; }
            if (data.ServiceName == "Consumption") { return [47.42882423, 54.04916975]; }
            if (data.ServiceName == "Employment") { return [33.13814798, 72.57176231]; }
            if (data.ServiceName == "Finance") { return [31.42250002, 61.56578545]; }
            if (data.ServiceName == "Innovation") { return [25.89488723, 65.3289721]; }
            if (data.ServiceName == "Production") { return [45.11697104, 51.67193166]; }
            if (data.ServiceName == "Re-Distribution") { return [23.51316313, 68.92691912]; }
            if (data.ServiceName == "Air Quality") { return [10, 90]; }
            if (data.ServiceName == "Food, Fiber, Fuel") { return [32.62908483, 48.49178319]; }
            if (data.ServiceName == "Greenspace") { return [36.11207908, 62.03906984]; }
            if (data.ServiceName == "Water Quality") { return [15.95637509, 88.22033237]; }
            if (data.ServiceName == "Water Quantity") { return [21.70976841, 72.83447998]; }
            if (data.ServiceName == "Activism") { return [25.85945275, 73.66346154]; }
            if (data.ServiceName == "Communication") { return [33.10020486, 68.98955269]; }
            if (data.ServiceName == "Community And Faith") { return [12.21375305,	90]; }
            if (data.ServiceName == "Education") { return [33.24429069,	56.47803694]; }
            if (data.ServiceName == "Emergency Preparedness") { return [19.78920564, 76.07510118]; }
            if (data.ServiceName == "Family Services") { return [42.66833596, 73.35259094]; }
            if (data.ServiceName == "Healthcare") { return [29.63020433, 62.25876617]; }
            if (data.ServiceName == "Justice") { return [31.22560175, 71.78167536]; }
            if (data.ServiceName == "Labor") { return [36.52332879, 53.29715035]; }
            if (data.ServiceName == "Public Works") { return [33.53645478, 66.4893089]; }
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
        
        dragVal.results.services[index].Score = value;
    }
}

//old GET request to calc endpoint
//function useServiceValues() {
//    //$.getJSON('api/HWBI?CapitalInvestmentScore=58.9&ConsumptionScore=51.6&EmploymentScore=52.3&FinanceScore=44.0&InnovationScore=43.24&ProductionScore=50.44&ReDistributionScore=47.2&AirQualityScore=19.2&FoodFiberAndFuelProvisioningScore=44.44&GreenspaceScore=42.6&WaterQualityScore=67.4&WaterQuantityScore=37.9&ActivismScore=48.9&CommunicationScore=43.4&CommunityAndFaithBasedInitiativesScore=15.81&EducationScore=45.0&EmergencyPreparednessScore=52.6&FamilyServicesScore=50.0&HealthcareScore=48.7&JusticeScore=42.76&LaborScore=40.82&PublicWorksScore=41.84&ConnectionToNatureDomainWeight=1.0&CulturalFulfillmentDomainWeight=1.0&EducationDomainWeight=1.0&HealthDomainWeight=1.0&LeisureTimeDomainWeight=1.0&LivingStandardsDomainWeight=1.0&SafetyAndSecurityDomainWeight=1.0&SocialCohesionDomainWeight=1.0', function (data) {
//    //http://134.67.114.8/hwbi/rest/hwbi/calc?CapitalInvestmentScore=58.9&ConsumptionScore=51.6&EmploymentScore=52.3&FinanceScore=44.0&InnovationScore=43.24&ProductionScore=50.44&ReDistributionScore=47.2&AirQualityScore=12.2&FoodFiberAndFuelProvisioningScore=44.44&GreenspaceScore=42.6&WaterQualityScore=67.4&WaterQuantityScore=37.9&ActivismScore=48.9&CommunicationScore=43.4&CommunityAndFaithBasedInitiativesScore=15.81&EducationScore=45.0&EmergencyPreparednessScore=52.6&FamilyServicesScore=50.0&HealthcareScore=48.7&JusticeScore=42.76&LaborScore=40.82&PublicWorksScore=41.84&ConnectionToNatureDomainWeight=1.0&CulturalFulfillmentDomainWeight=1.0&EducationDomainWeight=1.0&HealthDomainWeight=1.0&LeisureTimeDomainWeight=1.0&LivingStandardsDomainWeight=1.0&SafetyAndSecurityDomainWeight=1.0&SocialCohesionDomainWeight=1.0
//    $.getJSON('/hwbi/rest/hwbi/calc?CapitalInvestmentScore=' + dragVal.results.services[0].Score + '&ConsumptionScore=' + dragVal.results.services[1].Score + '&EmploymentScore=' + dragVal.results.services[2].Score + '&FinanceScore=' + dragVal.results.services[3].Score + '&InnovationScore=' + dragVal.results.services[4].Score + '&ProductionScore=' + dragVal.results.services[5].Score + '&ReDistributionScore=' + dragVal.results.services[6].Score + '&AirQualityScore=' + dragVal.results.services[7].Score + '&FoodFiberAndFuelProvisioningScore=' + dragVal.results.services[8].Score + '&GreenspaceScore=' + dragVal.results.services[9].Score + '&WaterQualityScore=' + dragVal.results.services[10].Score + '&WaterQuantityScore=' + dragVal.results.services[11].Score + '&ActivismScore=' + dragVal.results.services[12].Score + '&CommunicationScore=' + dragVal.results.services[13].Score + '&CommunityAndFaithBasedInitiativesScore=' + dragVal.results.services[14].Score + '&EducationScore=' + dragVal.results.services[15].Score + '&EmergencyPreparednessScore=' + dragVal.results.services[16].Score + '&FamilyServicesScore=' + dragVal.results.services[17].Score + '&HealthcareScore=' + dragVal.results.services[18].Score + '&JusticeScore=' + dragVal.results.services[19].Score + '&LaborScore=' + dragVal.results.services[20].Score + '&PublicWorksScore=' + dragVal.results.services[21].Score + '&ConnectionToNatureDomainWeight=' + dragVal.results.domains[0].Weight + '&CulturalFulfillmentDomainWeight=' + dragVal.results.domains[1].Weight + '&EducationDomainWeight=' + dragVal.results.domains[2].Weight + '&HealthDomainWeight=' + dragVal.results.domains[3].Weight + '&LeisureTimeDomainWeight=' + dragVal.results.domains[4].Weight + '&LivingStandardsDomainWeight=' + dragVal.results.domains[5].Weight + '&SafetyAndSecurityDomainWeight=' + dragVal.results.domains[6].Weight + '&SocialCohesionDomainWeight=' + dragVal.results.domains[7].Weight, function (data) {
//        updateDomainScores(data.Domains);
//        updateRIVWeights(dragVal.Domains);
//    });
//}


//POST request to calc endpoint
function useServiceValues() {
    var postData = {
        "scores" : {
            "CapitalInvestment": dragVal.results.services[0].Score,
            "Consumption": dragVal.results.services[1].Score,
            "Employment": dragVal.results.services[2].Score,
            "Finance": dragVal.results.services[3].Score,
            "Innovation": dragVal.results.services[4].Score,
            "Production": dragVal.results.services[5].Score,
            "ReDistribution": dragVal.results.services[6].Score,
            "AirQuality": dragVal.results.services[7].Score,
            "FoodFiberAndFuel": dragVal.results.services[8].Score,
            "Greenspace": dragVal.results.services[9].Score,
            "WaterQuality": dragVal.results.services[10].Score,
            "WaterQuantity": dragVal.results.services[11].Score,
            "Activism": dragVal.results.services[12].Score,
            "Communication": dragVal.results.services[13].Score,
            "CommunityAndFaith": dragVal.results.services[14].Score,
            "Education": dragVal.results.services[15].Score,
            "EmergencyPreparedness": dragVal.results.services[16].Score,
            "FamilyServices": dragVal.results.services[17].Score,
            "Healthcare": dragVal.results.services[18].Score,
            "Justice": dragVal.results.services[19].Score,
            "Labor": dragVal.results.services[20].Score,
            "PublicWorks": dragVal.results.services[21].Score
        },
        "domainWeights" : {
            "ConnectionToNature": dragVal.results.domains[0].Weight,
            "CulturalFulfillment": dragVal.results.domains[1].Weight,
            "Education": dragVal.results.domains[2].Weight,
            "Health": dragVal.results.domains[3].Weight,
            "LeisureTime": dragVal.results.domains[4].Weight,
            "LivingStandards": dragVal.results.domains[5].Weight,
            "SafetyAndSecurity": dragVal.results.domains[6].Weight,
            "SocialCohesion": dragVal.results.domains[7].Weight
        }
    };

    $.post(
        '/rest/hwbi/calc',                      // url
        JSON.stringify(postData),                               // data (as JS object)
        function(data) {                        // succuess (callback) funtion
            updateDomainScores(data.results.domains);
            updateRIVWeights(dragVal.results.domains);
    },
    "json");                                    // data type returned from server
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
}


//update sliders chart function
function updateSliders(data, index) {

    //set scale for slider. domain is input min max. range is slider translated min max (same)
var x = d3.scale.linear()
    .domain((function () {
            if (data.ServiceName == "Capital Investment") { return [56.31683197, 61.75389692]; }
            if (data.ServiceName == "Consumption") { return [47.42882423, 54.04916975]; }
            if (data.ServiceName == "Employment") { return [33.13814798, 72.57176231]; }
            if (data.ServiceName == "Finance") { return [31.42250002, 61.56578545]; }
            if (data.ServiceName == "Innovation") { return [25.89488723, 65.3289721]; }
            if (data.ServiceName == "Production") { return [45.11697104, 51.67193166]; }
            if (data.ServiceName == "Re-Distribution") { return [23.51316313, 68.92691912]; }
            if (data.ServiceName == "Air Quality") { return [10, 90]; }
            if (data.ServiceName == "Food, Fiber, Fuel") { return [32.62908483, 48.49178319]; }
            if (data.ServiceName == "Greenspace") { return [36.11207908, 62.03906984]; }
            if (data.ServiceName == "Water Quality") { return [15.95637509, 88.22033237]; }
            if (data.ServiceName == "Water Quantity") { return [21.70976841, 72.83447998]; }
            if (data.ServiceName == "Activism") { return [25.85945275, 73.66346154]; }
            if (data.ServiceName == "Communication") { return [33.10020486, 68.98955269]; }
            if (data.ServiceName == "Community And Faith") { return [12.21375305,	90]; }
            if (data.ServiceName == "Education") { return [33.24429069,	56.47803694]; }
            if (data.ServiceName == "Emergency Preparedness") { return [19.78920564, 76.07510118]; }
            if (data.ServiceName == "Family Services") { return [42.66833596, 73.35259094]; }
            if (data.ServiceName == "Healthcare") { return [29.63020433, 62.25876617]; }
            if (data.ServiceName == "Justice") { return [31.22560175, 71.78167536]; }
            if (data.ServiceName == "Labor") { return [36.52332879, 53.29715035]; }
            if (data.ServiceName == "Public Works") { return [33.53645478, 66.4893089]; }
        })()
    )
    .range([1, 99])
    //make scale *always* abide by range
    .clamp(true);

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