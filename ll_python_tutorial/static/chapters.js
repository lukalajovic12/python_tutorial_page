
$(document).ready(function(){
    $("#main").addClass("main_menu_open");
    $("#mySidenav").addClass("left_menu_open");
    $("#closeButton").click(function(){
            $("#mySidenav").removeClass("left_menu_open");
            $("#main").removeClass("main_menu_open");
             $("#mySidenav").addClass("left_menu_closed");
            $("#main").addClass("left_menu_closed");
  });
      $("#drawer").click(function(){
             $("#mySidenav").removeClass("left_menu_closed");
            $("#main").removeClass("main_menu_closed");
            $("#mySidenav").addClass("left_menu_open");
            $("#main").addClass("main_menu_open");
  });
      $('#pdf_button').click(function(){
        downloadPdf();
    });
});


function downloadPdf() {
    var doc = new jsPDF();
    var specialElementHandlers = {
    '#editor': function (element, renderer) {
        return true;
    }
    };

    doc.fromHTML($('#main').html(), 15, 15, {
        'width': 170,
    });
    doc.save('sample-file.pdf');
}




