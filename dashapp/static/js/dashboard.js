 function piechart(container, product, data) {
     Highcharts.chart(container, {
         chart: {
             plotBackgroundColor: null,
             plotBorderWidth: 1,
             plotShadow: false
         },
         title: {
             text: product,
             align: 'center',
             verticalAlign: 'middle',
             y: 90
         },
         tooltip: {
             pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
         },
        credits: {
         enabled: false
        },
         plotOptions: {
             pie: {
                 dataLabels: {
                     enabled: false,
                 },
                 startAngle: -110,
                 endAngle: 110,
                 center: ['50%', '75%'],
                 size: '110%'
             }
         },
         series: [{
             type: 'pie',
             name: 'Status',
             innerSize: '50%',
             data: data
         }]
     });

 }

 Highcharts.setOptions({
     colors: ['#3cd4a0', '#ff5c92', '#ffc260', '#536dfe']
 });

 piechart('prd-1', 'Android', [
     ['Pass', 70],
     ['Fail', 20],
     ['Not Tested', 10]
 ]);

 piechart('prd-2', 'iOS', [
     ['Pass', 75],
     ['Fail', 10],
     ['Not Tested', 15]
 ]);

 piechart('prd-3', 'Windows', [
     ['Pass', 60],
     ['Fail', 25],
     ['Not Tested', 15]
 ]);


 Highcharts.setOptions({
     colors: ['#7cb5ec', '#434348', '#90ed7d', '#f7a35c']
 });

 Highcharts.chart('prd-4', {
     chart: {
         type: 'bar',
         plotBorderWidth: 0,
     },

     title: {
         text: 'Bugs Reports'
     },
     subtitle: {
         text: 'newly created bugs on each release'
     },
     xAxis: {
         categories: ['Android', 'iOS', 'Windows'],
         title: {
             text: null
         }
     },
     yAxis: {
         min: 0,
         title: {
             text: 'Numbers of Bugs',
             align: 'high'
         },
         labels: {
             overflow: 'justify'
         }
     },

     plotOptions: {
         bar: {
             dataLabels: {
                 enabled: true
             }
         }
     },

     credits: {
         enabled: false
     },
     series: [{
         name: 'Release wk35',
         data: [30, 28, 17]
     }, {
         name: 'Release wk36',
         data: [33, 15, 27]
     }, {
         name: 'Release wk37',
         data: [14, 23, 37]
     }, {
         name: 'Release wk38',
         data: [10, 33, 14]
     }]
 });



 Highcharts.chart('prd-5', {

     title: {
         text: 'Bug Trends'
     },
     yAxis: {
         title: {
             text: 'Number of Bugs'
         }
     },
     xAxis: {
         accessibility: {
             rangeDescription: 'Range: 31 to 39'
         }
     },
     plotOptions: {
         series: {
             label: {
                 connectorAllowed: false
             },
             pointStart: 31
         }
     },
     credits: {
         enabled: false
     },
     series: [{
         name: 'Total Cpen',
         data: [40, 65, 68, 100, 95, 82, 79, 60]
     }, {
         name: 'Close',
         data: [5, 20, 32, 26, 28, 32, 12, 23]
     }, {
         name: 'In Progress',
         data: [22, 32, 52, 40, 48, 56, 50, 56]
     }, {
         name: 'Need info',
         data: [8, 15, 10, 19, 20, 6, 15, 22]
     }],

     responsive: {
         rules: [{
             condition: {
                 maxWidth: 500
             },
             chartOptions: {
                 legend: {
                     layout: 'horizontal',
                     align: 'center',
                     verticalAlign: 'bottom'
                 }
             }
         }]
     }

 });