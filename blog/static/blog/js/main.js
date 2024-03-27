$(function($) {
    $('#form_get_consultation').submit(function (e) {
        e.preventDefault()
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            dataType: 'json',
            success: function (response) {
                console.log('ok - ', response)
                if (response.hasOwnProperty('success')) {
                    $('.alert-success').removeClass('d-none').text(response.success)
                    $('.modal-title').text('Сообщение отправлено')
                    $('.close_consultation').removeClass('d-none')
                    $('#form_get_consultation').addClass('d-none')
                }
            },
            error: function (response) {
                console.log('err - ', response)
                if (response.status === 400) {
                    console.log('пришел 400')
                    var errors = JSON.parse(response.responseText);
                    if (errors.hasOwnProperty('error')) {
                        var errorData = JSON.parse(errors.error);
                        // Пройдемся по каждому полю формы и добавим сообщения об ошибках
                        Object.keys(errorData).forEach(function (key) {
                            var errorField = key;
                            console.log(errorField)
                            var errorMessage = errorData[key][0]; // Берем первое сообщение об ошибке, но можно обработать все
                            // Найдем соответствующее поле формы и добавим сообщение об ошибке
                            console.log(errorMessage['message'])
                            var fieldElement = $('[name="' + errorField + '"]');
                            console.log(fieldElement)
                            if (fieldElement.length) {
                                fieldElement.after('<div class="error-message" style="color:red;">' + errorMessage['message'] + '</div>' + '<br>');
                            }
                        });
                    }
                }
            }
        })
    });
    $('#form_get_consultation_main_page').submit(function (e) {
        e.preventDefault()
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            dataType: 'json',
            success: function (response) {
                console.log('ok - ', response)
                if (response.hasOwnProperty('success')) {
                    $('.alert-success').removeClass('d-none').text(response.success)
                    $('.modal-title').text('Сообщение отправлено')
                    $('.close_consultation').removeClass('d-none')
                    $('#form_get_consultation_main_page').addClass('d-none')
                }
            },
            error: function (response) {
                console.log('err - ', response)
                if (response.status === 400) {
                    console.log('пришел 400')
                    var errors = JSON.parse(response.responseText);
                    if (errors.hasOwnProperty('error')) {
                        var errorData = JSON.parse(errors.error);
                        // Пройдемся по каждому полю формы и добавим сообщения об ошибках
                        Object.keys(errorData).forEach(function (key) {
                            var errorField = key;
                            console.log(errorField)
                            var errorMessage = errorData[key][0]; // Берем первое сообщение об ошибке, но можно обработать все
                            // Найдем соответствующее поле формы и добавим сообщение об ошибке
                            console.log(errorMessage['message'])
                            var fieldElement = $('[name="' + errorField + '"]');
                            console.log(fieldElement)
                            if (fieldElement.length) {
                                fieldElement.after('<div class="error-message" style="color:red;">' + errorMessage['message'] + '</div>' + '<br>');
                            }
                        });
                    }
                }
            }
        })
    })
    $('.phone').mask('+7 (999) 999-99-99')

    $('#form_order_service').submit(function (e) {
        e.preventDefault()
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            dataType: 'json',
            success: function (response) {
                console.log('ok - ', response)
                if (response.hasOwnProperty('success')) {
                    $('.alert-success').removeClass('d-none').text(response.success)
                    $('.modal-title').text('Сообщение отправлено')
                    $('.close_consultation').removeClass('d-none')
                    $('#form_order_service').addClass('d-none')
                }
            },
            error: function (response) {
                console.log('err - ', response)
                if (response.status === 400) {
                    console.log('пришел 400')
                    var errors = JSON.parse(response.responseText);
                    if (errors.hasOwnProperty('error')) {
                        var errorData = JSON.parse(errors.error);
                        // Пройдемся по каждому полю формы и добавим сообщения об ошибках
                        Object.keys(errorData).forEach(function (key) {
                            var errorField = key;
                            console.log(errorField)
                            var errorMessage = errorData[key][0]; // Берем первое сообщение об ошибке, но можно обработать все
                            // Найдем соответствующее поле формы и добавим сообщение об ошибке
                            console.log(errorMessage['message'])
                            var fieldElement = $('[name="' + errorField + '"]');
                            console.log(fieldElement)
                            if (fieldElement.length) {
                                fieldElement.after('<div class="error-message" style="color:red;">' + errorMessage['message'] + '</div>' + '<br>');
                            }
                        });
                    }
                }
            }
        })
    })
    $('#form_training_order').submit(function (e) {
        e.preventDefault()
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            dataType: 'json',
            success: function (response) {
                console.log('ok - ', response)
                if (response.hasOwnProperty('success')) {
                    $('.alert-success').removeClass('d-none').text(response.success)
                    $('.modal-title').text('Сообщение отправлено')
                    $('.close_consultation').removeClass('d-none')
                    $('#form_training_order').addClass('d-none')
                }
            },
            error: function (response) {
                console.log('err - ', response)
                if (response.status === 400) {
                    console.log('пришел 400')
                    var errors = JSON.parse(response.responseText);
                    if (errors.hasOwnProperty('error')) {
                        var errorData = JSON.parse(errors.error);
                        // Пройдемся по каждому полю формы и добавим сообщения об ошибках
                        Object.keys(errorData).forEach(function (key) {
                            var errorField = key;
                            console.log(errorField)
                            var errorMessage = errorData[key][0]; // Берем первое сообщение об ошибке, но можно обработать все
                            // Найдем соответствующее поле формы и добавим сообщение об ошибке
                            console.log(errorMessage['message'])
                            var fieldElement = $('[name="' + errorField + '"]');
                            console.log(fieldElement)
                            if (fieldElement.length) {
                                fieldElement.after('<div class="error-message" style="color:red;">' + errorMessage['message'] + '</div>' + '<br>');
                            }
                        });
                    }
                }
            }
        })
    })
})

