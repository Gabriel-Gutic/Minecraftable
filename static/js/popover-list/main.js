class PopoverList {

    #ConstructorSetDefaults(options, defaults) {
        return $.extend({}, defaults, options || {});
    }
    constructor(options = {}) {
        if (!options.parent || !options.id) {
                console.error("PopoverList need a parent and an id!");
                return
        }
        
        let defaults = {
            parent: null,
            id: null,
            list_classes: "",
            popover_classes: "",
            special_component: function(type, id) { return ""; },
        }
        
        options = this.#ConstructorSetDefaults(options, defaults);    

        let customClass = options.list_classes.trim();
        this.#id = options.id;
        this.#content = `<ul id="` + options.id + `-list" class="list-group object-list mt-3 border border-light border-2 ` + customClass + `"></ul>`
        this.#parent = options.parent;
        this.#customClass = options.popover_classes.trim();
        this.#specialComponent = options.special_component;

        this.#parent.data("popover-list", this)

        this.SetPopover();
    }

    GetPopover() 
    {
        return $("." + this.#id);
    }

    SetPopover(placement = "right") 
    {
        this.Dispose();

        let customClass = "image-popover"
        if (this.#customClass != "")
            customClass += " " + this.#customClass;
        customClass += " " + this.#id; //put the popover id as a class
        this.#parent.popover({
            trigger: "manual",
            placement: placement,
            html: true,
            customClass: customClass,
            content: this.#content,
        })


    }

    UpdateContent() 
    {
        let parent = document.getElementById(this.#parent.attr("id"));
        let popover = bootstrap.Popover.getInstance(parent);

        popover._config.content = this.#content;
    }

    GetContent() 
    {
        return this.#content;
    }

    SetContent(content) 
    {
        this.#content = content;
        this.UpdateContent();
    }

    GetId() 
    {
        return this.#id
    }

    IsHovered() 
    {
        return this.GetPopover().is(":hover");
    }

    SetSpecialComponent(func) 
    {
        this.#specialComponent = func
    }

    #AddElementSetDefaults(options, defaults)
    {
        return $.extend({}, defaults, options || {});
    }

    AddElement(options) 
    {
        if (!options.type || !options.id || !options.name || !options.image)
        {
            console.error("There are missing some important values for element!");
        }

        let defaults = {
            type: null,
            id: null,
            name: null,
            image: null,
            extra_classes: "",
        };

        options = this.#AddElementSetDefaults(options, defaults);

        this.#content = this.#content.replace("</ul>", "")

        let element_id = this.#id + "-" + options.type + "-" + options.id;
        this.#content += `
        <li id="` + element_id + `" class="` + this.#id + `-element list-group-item d-flex justify-content-between align-items-center ` + options.extra_classes + `">
            <div id="` + element_id + `-div">` + this.#specialComponent(options.type, options.id) + options.name + `</div>
            <img id="` + element_id + `-image" src="` + options.image + `" class="element-image ms-2">
        </li>`

        this.#content += "</ul>"
        this.UpdateContent();
    }

    RemoveElement(type, id)
    {
        let string = type + "-" + id;

        let content = this.#content
        let position = content.indexOf(string)
        if (position > -1) 
        {
            let start_position = content.substring(0, position).lastIndexOf("<li")
            let end_position = content.indexOf("</li>", position) + 5;

            this.SetContent(content.replace(content.substring(start_position, end_position), ""))
        } 
    }

    ForEach(func){
        let content = this.GetContent()
        let i = 0;
        while(content.includes("<li"))
        {
            let start_position = content.indexOf("<li")
            let end_position = content.indexOf("</li>") + 5
            
            let element = content.substring(start_position, end_position)
            let doc = new DOMParser().parseFromString(element, "text/html")

            func(i, doc.body.firstElementChild)

            content = content.substring(end_position + 1, content.length)
            i++;
        }
    }

    Show() 
    {
        this.#parent.popover("show");
    }

    Hide() 
    {
        this.#parent.popover("hide");
    }

    Dispose() 
    {
        this.#parent.popover("dispose");
    }

    OnShow(func) 
    {
        this.#parent.off("shown.bs.popover").on("shown.bs.popover", func);
    }

    OnHide(func) 
    {
        this.#parent.off("hidden.bs.popover").on("hidden.bs.popover", func);
    }

    OnMouseEnterParent(func) 
    {
        this.#parent.off("mouseenter").on("mouseenter", func);
    }

    OnMouseLeaveParent(func) 
    {
        this.#parent.off("mouseleave").on("mouseleave", func);
    }

    OnMouseEnter(func) 
    {
        this.GetPopover().off("mouseenter").on("mouseenter", func);
    }

    OnMouseLeave(func) 
    {
        this.GetPopover().off("mouseleave").on("mouseleave", func);
    }

    SetPredifinedTrigger(nameClass, timeout = 200) 
    {
        let this_ = this
        this.OnMouseEnterParent(function(e) 
        {
            HidePopoversByClass(nameClass);

            this_.Show();

            $("." + nameClass).on("mouseleave", function() 
            {
                this_.Hide();
            });
        })
        this.OnMouseLeaveParent(function(e) 
        {
            setTimeout(function() {
                if (!$("." + nameClass + ".popover:hover").length) {
                    this_.Hide();
                }
            }, timeout)
        })
    }

    Size() 
    {
        return (this.#content.match(/<li/g) || []).length
    }

    #id;
    #content;
    #parent;
    #customClass;
    #specialComponent;
}