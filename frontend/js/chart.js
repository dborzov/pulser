      (function () {

        var
          container = document.getElementById('container2'),
          x = [],
          y1 = [],
          y2 = [],
          data, options, i;

        // Data Format:
        data = [
          [x_data, y_data]  // Second Series
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

