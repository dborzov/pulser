      (function () {

        var
          container = document.getElementById('container2'),
          x = [],
          y1 = [],
          y2 = [],
          data, options, i;

        // Data Format:
        data = [
          [x_data[1], y_data[1]]  // Second Series
        ];

        // Sample the sine function for data
        for (i = 0; i < 4 * Math.PI; i += 0.05) {
          x.push(i);
          y1.push(Math.sin(i));
          y2.push(Math.sin(i + Math.PI));
        }
        x.push(4 * Math.PI)
        y1.push(Math.sin(4 * Math.PI));
        y2.push(Math.sin(4 * Math.PI));

        // TimeSeries Template Options
        options = {
          container : container,
          // Data for detail (top chart) and summary (bottom chart)
          data : {
            detail : data,
            summary : data
          }
        };

        // Hey there! Browsin' my code? Why, I am flattered :)
        // Create the TimeSeries
        new envision.templates.TimeSeries(options);

      })();


    (function finance_demo (container) {

    options = {
    container : container,
    data : {
      price : y_data,
      volume : y_data,
      summary : y_data
    },
    trackFormatter : function (o) {
    var
        data = o.series.data,
        index = data[o.index][0],
        value;
    value = actually_data[index] + ' tweets';
      return value;
    },
    xTickFormatter : function (index) {
      return data_labels[index];
    },
    // An initial selection
    selection : {
      data : {
        x : {
          max : 25,
          min : 35
        }
      }
    }
  };

  return new envision.templates.Finance(options);
}
)(document.getElementById("editor-render-0"));

