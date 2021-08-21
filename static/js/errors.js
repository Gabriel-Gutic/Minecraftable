function Error(message) {

    $("#errors-content").append(`
    <div class="error-message alert alert-warning d-flex align-items-center alert-dismissible fade show ms-auto me-auto" role="alert">
                <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Warning:"><use xlink:href="#exclamation-triangle-fill"/></svg>
                <div>
                    ` + message + `
                </div>
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
    `);

}