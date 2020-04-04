document.addEventListener('DOMContentLoaded',
    function () {
        pointFormat: '{point.y} new cases were reported on {point.name}, bringing the total to {point.x}.'
        Highcharts.setOptions({
            lang: {
                numericSymbols: null //otherwise by default ['k', 'M', 'G', 'T', 'P', 'E']
            }
        });

        var myChart = Highcharts.chart('container', {
            chart: {
                type: 'scatter',
                zoomType: 'xy'
            },
            title: {
                text: null
            },
            xAxis: {
                type: 'logarithmic',
                title: {
                    enabled: true,
                    text: 'Total cases'
                },
                startOnTick: true,
                endOnTick: true,
                showLastLabel: true
            },
            yAxis: {
                type: 'logarithmic',
                title: {
                    text: 'New cases per day'
                }
            },
            plotOptions: {
                series: {
                    lineWidth: 2
                },
                scatter: {
                    marker: {
                        radius: 5,
                        states: {
                            hover: {
                                enabled: true,
                                lineColor: 'rgb(100,100,100)'
                            }
                        }
                    },
                    states: {
                        hover: {
                            marker: {
                                enabled: false
                            }
                        }
                    },
                    tooltip: {
                        headerFormat: '<b>{series.name}</b><br>',
                        pointFormat: '{point.y} new cases were reported on {point.name}, bringing the total to {point.x}.'
                    }
                }
            },
            series: series_data
        });
    }); // end function