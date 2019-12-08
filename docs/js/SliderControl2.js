L.Control.SliderControl2 = L.Control.extend({
    options: {
        position: 'topright',
        layers: null,
        timeAttribute: 'time',
        isEpoch: false,     // whether the time attribute is seconds elapsed from epoch
        startTimeIdx: 0,    // where to start looking for a timestring
        timeStrLength: 19,  // the size of  yyyy-mm-dd hh:mm:ss - if millis are present this will be larger
        maxValue: -1,
        minValue: 0,
        showAllOnStart: false,
        markers: null,
        range: false,
        follow: false,
        sameDate: false,
        alwaysShowDate : false,
        rezoom: null,
        sliderId: 1,
        sliderFullId2: null,
        sliderTimeStampId2: null,
        map: null
    },

    initialize: function (options) {
        L.Util.setOptions(this, options);
        this._layer = this.options.layer;

    },

    extractTimestamp: function(time, options) {
        if (options.isEpoch) {
            time = (new Date(parseInt(time))).toString(); // this is local time
        }
        return time.substr(options.startTimeIdx, options.startTimeIdx + options.timeStrLength);
    },

    setPosition: function (position) {
        var map = this._map;

        if (map) {
            map.removeControl(this);
        }

        this.options.position = position;

        if (map) {
            map.addControl(this);
        }
        this.startSlider();
        return this;
    },

    onAdd: function (map) {
        var options = this.options;
        this.options.map = map;
        this.options.sliderFullId2 = "#leaflet-slider" + this.options.sliderId;
        this.options.sliderTimeStampId2 = "#slider-timestamp" + this.options.sliderId;

        // Create a control sliderContainer with a jquery ui slider
        var sliderContainer = L.DomUtil.create('div', 'slider mright ' + this.options.sliderId, this._container);
        $(sliderContainer).append('<div id="leaflet-slider' + this.options.sliderId + '" style="width:200px"><div class="ui-slider-handle"></div><div id="slider-timestamp' + this.options.sliderId + '" style="width:200px; margin-top:20px; background-color:#FFFFFF; text-align:center; border-radius:5px;"></div></div>');

        //Prevent map panning/zooming while using the slider
        // $(sliderContainer).mousedown(function () {
        //     map.dragging.disable();
        // });
        $(document).mouseup(function () {
            // map.dragging.enable();
            //Hide the slider timestamp if not range and option alwaysShowDate is set on false
            if (options.range || !options.alwaysShowDate) {
                $(options.sliderTimeStampId2).html('');
            }
        });

        this.options.markers = [];

        //If a layer has been provided: calculate the min and max values for the slider
        if (this._layer) {
            var index_temp = 0;
            this._layer.eachLayer(function (layer) {
                options.markers[index_temp] = layer;
                ++index_temp;
            });
            options.maxValue = index_temp - 1;
            this.options = options;
        } else {
            console.log("Error: You have to specify a layer via new SliderControl({layer: your_layer});");
        }

        return sliderContainer;
    },

    onRemove: function (map) {
        //Delete all markers which where added via the slider and remove the slider div
        for (i = this.options.minValue; i <= this.options.maxValue; i++) {
            map.removeLayer(this.options.markers[i]);
        }
        $(this.options.sliderFullId2).remove();

        // unbind listeners to prevent memory leaks
        $(document).off("mouseup");
        $(".slider").off("mousedown");
    },

    startSlider: function () {
        _options2 = this.options;
        _extractTimestamp = this.extractTimestamp
        var index_start = _options2.maxValue;
        if(_options2.showAllOnStart){
            index_start = _options2.maxValue;
            if(_options2.range) _options2.values = [_options2.minValue,_options2.maxValue];
            else _options2.value = _options2.maxValue;
        }
        $(_options2.sliderFullId2).slider({
            range: _options2.range,
            value: _options2.maxValue,
            values: _options2.values,
            min: _options2.minValue,
            max: _options2.maxValue,
            sameDate: _options2.sameDate,
            step: 1,
            slide: function (e, ui) {
                var map = _options2.map;
                var fg = L.featureGroup();
                if(!!_options2.markers[ui.value]) {
                    // If there is no time property, this line has to be removed (or exchanged with a different property)
                    if(_options2.markers[ui.value].feature !== undefined) {
                        if(_options2.markers[ui.value].feature.properties[_options2.timeAttribute]){
                            if(_options2.markers[ui.value]) $(_options2.sliderTimeStampId2).html(
                                _extractTimestamp(_options2.markers[ui.value].feature.properties[_options2.timeAttribute], _options2));
                        }else {
                            console.error("Time property "+ _options2.timeAttribute +" not found in data");
                        }
                    }else {
                        // set by leaflet Vector Layers
                        if(_options2.markers [ui.value].options[_options2.timeAttribute]){
                            if(_options2.markers[ui.value]) $(_options2.sliderTimeStampId2).html(
                                _extractTimestamp(_options2.markers[ui.value].options[_options2.timeAttribute], _options2));
                        }else {
                            console.error("Time property "+ _options2.timeAttribute +" not found in data");
                        }
                    }

                    var i;
                    // clear markers
                    for (i = _options2.minValue; i <= _options2.maxValue; i++) {
                        if(_options2.markers[i]) map.removeLayer(_options2.markers[i]);
                    }
                    if(_options2.range){
                        // jquery ui using range
                        for (i = ui.values[0]; i <= ui.values[1]; i++){
                           if(_options2.markers[i]) {
                               map.addLayer(_options2.markers[i]);
                               fg.addLayer(_options2.markers[i]);
                           }
                        }
                    }else if(_options2.follow){
                        for (i = ui.value - _options2.follow + 1; i <= ui.value ; i++) {
                            if(_options2.markers[i]) {
                                map.addLayer(_options2.markers[i]);
                                fg.addLayer(_options2.markers[i]);
                            }
                        }
                    }else if(_options2.sameDate){
                        var currentTime;
                        if (_options2.markers[ui.value].feature !== undefined) {
                            currentTime = _options2.markers[ui.value].feature.properties.time;
                        } else {
                            currentTime = _options2.markers[ui.value].options.time;
                        }
                        for (i = _options2.minValue; i <= _options2.maxValue; i++) {
                            if(_options2.markers[i].options.time == currentTime) map.addLayer(_options2.markers[i]);
                        }
                    }else{
                        for (i = _options2.minValue; i <= ui.value ; i++) {
                            if(_options2.markers[i]) {
                                map.addLayer(_options2.markers[i]);
                                fg.addLayer(_options2.markers[i]);
                            }
                        }
                    }
                };
                if(_options2.rezoom) {
                    map.fitBounds(fg.getBounds(), {
                        maxZoom: _options2.rezoom
                    });
                }
            }
        });
        if (!_options2.range && _options2.alwaysShowDate) {
            $(_options2.sliderTimeStampId2).html(_extractTimeStamp(_options2.markers[index_start].feature.properties[_options2.timeAttribute], _options2));
        }
        for (i = _options2.maxValue; i <= index_start; i++) {
            _options2.map.addLayer(_options2.markers[i]);
        }
    }
});

L.control.sliderControl2 = function (options) {
    return new L.Control.SliderControl2(options);
};
