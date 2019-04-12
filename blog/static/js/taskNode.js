  $(onPageLoad);

  function onPageLoad()
  {
    $( ".column" ).sortable({
      connectWith: ".column",
      handle: ".portlet-header",
      cancel: ".portlet-toggle",
      start: function (event, ui) {
        ui.item.addClass('tilt');
      },
      stop: function (event, ui) {
        ui.item.removeClass('tilt');
      }
    });
//    Делаем скрытый список
    $( ".portlet-content" )
        .toggle();




    $( ".portlet" )
      .addClass( "ui-widget ui-widget-content ui-helper-clearfix ui-corner-all" )
      .find( ".portlet-header" )
        .addClass( "ui-widget-header ui-corner-all" )
        .prepend( "<span class='ui-icon ui-icon-minusthick portlet-toggle'></span>");

//клик по иконке скрывательной
    $( ".portlet-toggle" ).click(function() {
               var icon = $( this );
               icon.toggleClass( "ui-icon-minusthick ui-icon-plusthick" );
               icon.closest( ".portlet" ).find( ".portlet-content" ).toggle();

             });
  }

//    $( ".portlet-toggle" ).dblclick()(function() {
//            var icon = $( this );
//            icon.toggleClass( "ui-icon-minusthick ui-icon-plusthick" );
//            icon.closest( ".portlet" ).find( ".portlet-content" ).toggle();
//
//        });
//    }