function load_map(ticks, path, colors, id_div, centre_point, info_string, info_string2, zoom, id_slider, layergroupHolder, mapHolder) {

    function getColor(d, year) {
        for (var i=ticks[year].length-2; i>=0; i--) {
            if (Math.round(d) >= ticks[year][i])
                return colors[i];
        }
    }

    function style(feature) {
        return {
            fillColor: getColor(feature.properties.val, feature.properties.year),
            weight: 0.5,
            opacity: 0.7,
            color: '#000000',
            dashArray: '2',
            fillOpacity: 0.7
        };
    }

    function highlightFeature(e) {
        var layer = e.target;

        layer.setStyle({
            weight: 1.5,
            color: '#666',
            dashArray: '',
            fillOpacity: 0.8
        });

        info.update(layer.defaultOptions.time, layer.feature.properties);

        if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
            layer.bringToFront();
        }
    }

    function resetHighlight(e) {
        layergroupHolder['layergroup' + id_slider].eachLayer(function (layer) {
            layer.resetStyle(e.target);
        });
        info.update(e.target.defaultOptions.time);
    }

    function setLegendInfo(e) {
        var layer = e.target;
        legend.update(layer.defaultOptions.time, ticks);
        info.update(layer.defaultOptions.time);
    }

    function onEachFeature(feature, layer) {
        layer.on({
            mouseover: highlightFeature,
            mouseout: resetHighlight,
            add: setLegendInfo
        });
    }

    var info = L.control({position: 'bottomleft'});

    info.onAdd = function (map) {
        this._div = L.DomUtil.create('div', 'info fix_height');
        return this._div;
    };

    info.update = function (time, props) {
        this._div.innerHTML = '<h4>' + info_string + " " + time + '</h4>'+  (props ?
            '<b>' + props.name + '</b><br /><b>' + props.val.toFixed(2) + ' </b>' + info_string2
            : 'Hover over a state');
    };

    var legend = L.control({position: 'bottomright'});

    legend.onAdd = onAddLegend();

    function onAddLegend() {
        return function(map) {
            this._div = L.DomUtil.create('div', 'info legend');
            return this._div;
        };
    };

    legend.update = function (year, props) {
            end_len = props[year].length - 1;
            grades = props[year].slice(0, end_len);
            labels = [];
            this._div.innerHTML = '';
            for (var i = 0; i < grades.length; i++) {
                this._div.innerHTML +=
                    '<i style="background:' + getColor(grades[i] + 1, year) + '"></i> ' +
                    grades[i] + ((grades[i + 1] || grades[i+1]==0) ? ' &ndash; ' + grades[i + 1] + '<br>' : '+');
            }
    };

    mapHolder['map' + id_slider] = L.map(id_div, { zoomControl: false }).setView(centre_point, zoom);

    mapHolder['map' + id_slider].touchZoom.disable();
    mapHolder['map' + id_slider].doubleClickZoom.disable();
    mapHolder['map' + id_slider].scrollWheelZoom.disable();
    mapHolder['map' + id_slider].boxZoom.disable();
    mapHolder['map' + id_slider].keyboard.disable();
    mapHolder['map' + id_slider].dragging.disable();

    L.tileLayer('https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}{r}.png', {
        id: 'mapbox/light-v9',
        attribution: ''
    }).addTo(mapHolder['map' + id_slider]);

    layergroupHolder['layergroup' + id_slider] = L.layerGroup();
    if (id_slider==-1) {
        var geojsonLayer = new L.GeoJSON.AJAX(path,{
            style: style,
            onEachFeature: onEachFeature,
            time: "2020"
        });
        layergroupHolder['layergroup' + id_slider].addLayer(geojsonLayer);
        info.addTo(mapHolder['map' + id_slider]);
        legend.addTo(mapHolder['map' + id_slider]);
        geojsonLayer.addTo(mapHolder['map' + id_slider]);
        mapHolder['map' + id_slider].dragging.enable();
        L.DomUtil.addClass(mapHolder['map' + id_slider]._container,'crosshair-cursor-enabled');
        return;
    }

    for (var i = 1961; i<=2020; i++) {
        layergroupHolder['layergroup' + id_slider].addLayer(new L.GeoJSON.AJAX(path + i + ".geojson",{
        style: style,
        onEachFeature: onEachFeature,
        time: i.toString()
    }));
    }

    switch(id_slider) {
        case 1:
            slider = L.control.sliderControl({layer:layergroupHolder['layergroup' + id_slider], follow: 1, position:"topright", sliderId: id_slider});
            break;
        case 2:
            slider = L.control.sliderControl2({layer:layergroupHolder['layergroup' + id_slider], follow: 1, position:"topright", sliderId: id_slider});
            break;
        case 3:
            slider = L.control.sliderControl3({layer:layergroupHolder['layergroup' + id_slider], follow: 1, position:"topright", sliderId: id_slider});
            break;
        case 4:
            slider = L.control.sliderControl4({layer:layergroupHolder['layergroup' + id_slider], follow: 1, position:"topright", sliderId: id_slider});
            break;
      }

    
    info.addTo(mapHolder['map' + id_slider]);
    legend.addTo(mapHolder['map' + id_slider]);
    mapHolder['map' + id_slider].addControl(slider);//add slider to map
    slider.startSlider();//starting slider
    L.DomUtil.addClass(mapHolder['map' + id_slider]._container,'crosshair-cursor-enabled');
}