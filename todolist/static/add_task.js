$(document).ready(function () {
    $("#add_task").submit(function (event) {
      var formData = {
        title: $("#title").val(),
        description: $("#description").val(),
      };
  
      $.ajax({
        type: "POST",
        url: "{% url 'todolist' %}",
        data: formData,
        dataType: "json",
        encode: true,
      }).done(function (data) {
        console.log(data);
      });
  
      event.preventDefault();
    });
  });