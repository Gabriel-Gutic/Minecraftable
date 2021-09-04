class Modal 
{
    #id;

    #SetDefaultOptions(options, defaults)
    {
        return $.extend({}, defaults, options || {});
    }

    constructor($parent, id)
    {
        this.#id = id;

        $parent.append(`
        <div id="` + this.#id + `" class="modal fade" tabindex="-1" aria-labelledby="` + this.#id + `-label" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="` + this.#id + `-label">Title</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                    </div>
                    <div class="modal-footer">
                    </div>
                </div>
            </div>
        </div>`)
    }

    Get$Label()
    {
        return $("#" + this.#id + "-label");
    }

    SetTitle(title)
    {
        this.Get$Label().text(title);
    }

    GetTitle()
    {
        return this.Get$Label().text();
    }

    Get$Body()
    {
        return $("#" + this.#id).find(".modal-body");
    }

    Get$Footer()
    {
        return $("#" + this.#id).find(".modal-footer");
    }

    AddButton(options)
    {
        if (!options.id)
            console.error("Modal Button must have an id!")
        let defaults = {
            classes: "",
            text: "",
        }

        options = this.#SetDefaultOptions(options, defaults);

        this.Get$Footer().append(`<button id="` + options.id + `" type="button" class="` + options.classes + `">` + options.text + `</button>`)
    }

    Get$Button(id)
    {
        return $("#" + id);
    }

    SetButtonForClose(id)
    {
        this.Get$Button(id).attr("data-bs-dismiss", "modal");
    }

    Show()
    {
        $("#" + this.#id).modal("show");
    }

    Hide()
    {
        $("#" + this.#id).modal("hide");
    }
}

jQuery.fn.extend({

    modalObject: function(id="")
    {
        if (id == "")
            return $(this).data("modal-object");
        
        let modal_object = new Modal($(this), id);
        $(this).data("modal-object", modal_object);
        return $(this).data("modal-object");
    }

})