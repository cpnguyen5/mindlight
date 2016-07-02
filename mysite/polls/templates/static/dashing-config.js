//var dashboard = new Dashboard();
//
//dashboard.addWidget('clock_widget', 'Clock');
//

var dashboard = new Dashboard();

dashboard.addWidget('clock_widget', 'Clock');

//var myDashboard = new Dashboard();
Dashboard.addWidget('customWidget', 'Number', {
    getData: function () {
        var self = this;
        Dashing.utils.get('custom_widget', function(data) {
            $.extend(self.scope, data);
        });
    },
    interval: 3000
});