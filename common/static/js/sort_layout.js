$(() => {
    
    // initialization

    // add toggle display button
    $(".entity-sort").each((i, e) => {
        if ($(e).data("visibility") === undefined) {
            $(e).data("visibility", true);
        }
        let btn = $("#toggleDisplayButtonTemplate").clone().removeAttr("id");
        btn.click(e => {
            if ($(e.currentTarget).parent().data('visibility') === true) {                
                // flip text
                $(e.currentTarget).children("span.showText").show();
                $(e.currentTarget).children("span.hideText").hide();
                // flip data
                $(e.currentTarget).parent().data('visibility', false);
                // flip display
                $(e.currentTarget).parent().addClass("entity-sort--hidden");
            } else {
                // flip text
                $(e.currentTarget).children("span.showText").hide();
                $(e.currentTarget).children("span.hideText").show();
                // flip data
                $(e.currentTarget).parent().data('visibility', true);
                // flip display
                $(e.currentTarget).parent().removeClass("entity-sort--hidden");
            }
        });
        $(e).prepend(btn);
    });
    // initialize toggle buttons
    initialLayoutData.forEach(elem => {
        if (elem.visibility) {
            $('#' + elem.id).find("span.showText").hide();
            $('#' + elem.id).find("span.hideText").show();
        } else {
            $('#' + elem.id).find("span.showText").show();
            $('#' + elem.id).find("span.hideText").hide();
        }
    });
    // initialize the sortable plugin
    sortable('.sortable', {
        forcePlaceholderSize: true,
        placeholderClass: 'entity-sort--placeholder',
        // hoverClass: 'entity-sort--hover'
    });
    sortable('.sortable', 'disable');
    // set state flag
    let isActivated = false;
    // set class modifier, because the effect of the plugin is not very well
    let dragging = false;
    $(".entity-sort").on('mouseenter', (e) => {
        if (isActivated && !dragging) {
            $(e.currentTarget).addClass("entity-sort--hover");
        }
    });
    $(".entity-sort").on('mouseleave', (e) => {
        if (isActivated) {
            $(e.currentTarget).removeClass("entity-sort--hover");
        }
    });
    $(".entity-sort").on('dragstart', (e) => {
        if (isActivated) {
            dragging = true;
        }
    });
    $(".entity-sort").on('dragend', (e) => {
        if (isActivated) {
            dragging = false;
        }
    });


    // activate sorting
    $("#sortEditButton").click(e => {
        // test if edit mode is activated
        isActivated = $("#sortSaveIcon").is(":visible");

        if (isActivated) {
            // save edited layout

            let rawData = sortable('.sortable', 'serialize')[0].items;
            let serializedData = []

            // collect layout information
            for (const key in rawData) {
                if (Object.hasOwnProperty.call(rawData, key)) {
                    const sort = rawData[key];
                    let id = $(sort.node).attr("id");
                    let visibility = $(sort.node).data("visibility") ? true : false;
                    serializedData.push({
                        id: id,
                        visibility: visibility
                    });
                }
            }
            $("#sortForm input[name='layout']").val(JSON.stringify(serializedData))
            $("#sortForm").submit();
            // console.log(serializedData)


        } else {
            // enter edit mode
            $("#sortSaveIcon").show();
            $("#sortEditIcon").hide();
            $("#sortSaveText").show();
            $("#sortEditText").hide();
            $("#sortExitButton").show();
            sortable('.sortable', 'enable');
            $(".entity-sort").each((index, elem) => {
                $(elem).show();
                $(elem).addClass("entity-sort--sortable");
                if ($(elem).data('visibility') === true) {
                    $(elem).find("span.showText").hide();
                    $(elem).find("span.hideText").show();
                } else if ($(elem).data('visibility') === false) {
                    $(elem).find("span.showText").show();
                    $(elem).find("span.hideText").hide();
                }
                $(elem).children(".entity-sort-control__button").show();
                if ($(elem).data('visibility') === false) {
                    $(elem).addClass("entity-sort--hidden");
                }
            });
        }
        isActivated = $("#sortSaveIcon").is(":visible");
    });
    
    // exit edit mode
    $("#sortExitButton").click(e => {
        $("#sortSaveIcon").hide();
        $("#sortEditIcon").show();
        $("#sortSaveText").hide();
        $("#sortEditText").show();
        $("#sortExitButton").hide();
        sortable('.sortable', 'disable');
        $(".entity-sort").each((index, elem) => {
            $(elem).removeClass("entity-sort--sortable");
        });
        isActivated = $("#sortSaveIcon").is(":visible");
    });
});