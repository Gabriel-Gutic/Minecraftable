class ElementList {
    constructor(element, type) {
        this.input = `<div id="` + type + `-line-` + element.id + `">
        <input class="form-check-input" type="radio" name="data-radio-list" id="radio-` + type + `-` + element.id + `" value="` + element.id + `~` + element.image + `"> 
            <label id="label-` + type + `-` + element.id + `" class="form-check-label ms-2" for="radio-` + type + `-` + element.id + `">
           ` + element.name + `
            </label>
        </div>`
        this.type = type;
        this.image = null;
        if (element.image != null && element.image != "None") {
            this.image = `<img id="` + type + `-image-` + element.id + `" src="` + element.image + `" class="` + type + `-image element-image" loading="lazy">`
        }
    }
}