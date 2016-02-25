var height = 82,
    width = 1000;

var svg = d3.select("#flowchart").append("svg")
        .attr("height", height)
        .attr("width", width)

var rectangles = [
{ Rect: '22 Services', url: "http://www.epa.gov", x: '10'},
{ Rect: '8 Domains', url: "http://www.epa.gov", x: '10'},
{ Rect: 'Relative Importance Values', url: "http://www.epa.gov", x: '10'}
];


//services rectangle
var rect = svg.append("a")
    .attr("transform", "translate(1,10)")
    .attr("xlink:href", "http://www.epa.gov")
    .append("rect")
    .attr("height", 60)
    .attr("width", 90)
    .attr("rx", 10)
    .attr("ry", 10)
    .attr("fill", "#FFFFFF")
    .attr("stroke", "gray");

svg.append("svg:text")
          .style("pointer-events", "none")
    .attr("transform", "translate(0,10)")
  .attr("class", "score")
  .attr("dy", 35)
  .attr("dx", 45)
  .attr("text-anchor", "middle")
  .attr("font-size", "15px")
  .text("22 Services");

//domains rectangle
var rect = svg.append("a")
    .attr("transform", "translate(120,10)")
    .attr("xlink:href", "http://www.epa.gov")
    .append("rect")
    .attr("height", 60)
    .attr("width", 90)
    .attr("rx", 10)
    .attr("ry", 10)
    .attr("fill", "#FFFFFF")
    .attr("stroke", "gray");

svg.append("svg:text")
      .style("pointer-events", "none")
      .attr("transform", "translate(120,10)")
      .attr("class", "score")
      .attr("dy", 35)
      .attr("dx", 45)
      .attr("text-anchor", "middle")
      .attr("font-size", "15px")
      .text("8 Domains");

//RIV rectangle
var rect = svg.append("a")
    .attr("transform", "translate(240,10)")
    .attr("xlink:href", "http://www.epa.gov")
    .append("rect")
    .attr("height", 60)
    .attr("width", 90)
    .attr("rx", 10)
    .attr("ry", 10)
    .attr("fill", "#FFFFFF")
    .attr("stroke", "gray");

svg.append("svg:text")
    .style("pointer-events", "none")
    .attr("transform", "translate(240,10)")
  .attr("class", "score")
  .attr("dy", 18)
  .attr("dx", 45)
  .attr("text-anchor", "middle")
  .attr("font-size", "15px")
  .text("Relative");

svg.append("svg:text")
          .style("pointer-events", "none")
    .attr("transform", "translate(240,10)")
  .attr("class", "score")
  .attr("dy", 35)
  .attr("dx", 45)
  .attr("text-anchor", "middle")
  .attr("font-size", "15px")
  .text("Importance");

svg.append("svg:text")
          .style("pointer-events", "none")
    .attr("transform", "translate(240,10)")
  .attr("class", "score")
  .attr("dy", 52)
  .attr("dx", 45)
  .attr("text-anchor", "middle")
  .attr("font-size", "15px")
  .text("Values");

//hwbi circle
var hwbicirc = svg.append("a")
    .attr("transform", "translate(360,0)")
    .attr("xlink:href", "http://www.google.com")
    .append("circle")
    .attr("r", 35)
    .attr("cx", 36)
    .attr("cy", 41)
    .attr("fill", "#FFFFFF")
    .attr("stroke", "gray");

svg.append("svg:text")
          .style("pointer-events", "none")
    .attr("transform", "translate(360,0)")
  .attr("class", "score")
  .attr("dy", 46)
  .attr("dx", 36)
  .attr("text-anchor", "middle")
  .attr("font-size","17px")
  .style("font-weight", "bold")
  .text("HWBI");


//arrow 1
var arrowYPosition = 40
var arrowXStartPosition = 91
var arrowXEndPosition = 119;

var labelLine = svg.append("line")
        .attr("x1", arrowXStartPosition)
        .attr("y1", arrowYPosition)
        .attr("x2", arrowXEndPosition)
        .attr("y2", arrowYPosition)
        .attr("stroke-width", 2)
        .attr("stroke", "gray");

var right = svg.append("line")
        .attr("x1", arrowXEndPosition)
        .attr("y1", arrowYPosition)
        .attr("x2", arrowXEndPosition - 10)
        .attr("y2", arrowYPosition + 10)
        .attr("stroke-width", 2)
        .attr("stroke", "gray");

var left = svg.append("line")
        .attr("x1", arrowXEndPosition)
        .attr("y1", arrowYPosition)
        .attr("x2", arrowXEndPosition - 10)
        .attr("y2", arrowYPosition - 10)
        .attr("stroke-width", 2)
        .attr("stroke", "gray");

//arrow 2
var arrowYPosition = 40
var arrowXStartPosition = 210
var arrowXEndPosition = 240;

var labelLine = svg.append("line")
        .attr("x1", arrowXStartPosition)
        .attr("y1", arrowYPosition)
        .attr("x2", arrowXEndPosition)
        .attr("y2", arrowYPosition)
        .attr("stroke-width", 2)
        .attr("stroke", "gray");

var right = svg.append("line")
        .attr("x1", arrowXEndPosition)
        .attr("y1", arrowYPosition)
        .attr("x2", arrowXEndPosition - 10)
        .attr("y2", arrowYPosition + 10)
        .attr("stroke-width", 2)
        .attr("stroke", "gray");

var left = svg.append("line")
        .attr("x1", arrowXEndPosition)
        .attr("y1", arrowYPosition)
        .attr("x2", arrowXEndPosition - 10)
        .attr("y2", arrowYPosition - 10)
        .attr("stroke-width", 2)
        .attr("stroke", "gray");

//arrow 3
var arrowYPosition = 40
var arrowXStartPosition = 330
var arrowXEndPosition = 360;

var labelLine = svg.append("line")
        .attr("x1", arrowXStartPosition)
        .attr("y1", arrowYPosition)
        .attr("x2", arrowXEndPosition)
        .attr("y2", arrowYPosition)
        .attr("stroke-width", 2)
        .attr("stroke", "gray");

var right = svg.append("line")
        .attr("x1", arrowXEndPosition)
        .attr("y1", arrowYPosition)
        .attr("x2", arrowXEndPosition - 10)
        .attr("y2", arrowYPosition + 10)
        .attr("stroke-width", 2)
        .attr("stroke", "gray");

var left = svg.append("line")
        .attr("x1", arrowXEndPosition)
        .attr("y1", arrowYPosition)
        .attr("x2", arrowXEndPosition - 10)
        .attr("y2", arrowYPosition - 10)
        .attr("stroke-width", 2)
        .attr("stroke", "gray");