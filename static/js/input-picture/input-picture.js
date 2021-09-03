class InputPicture
{
    #id;
    #text;
    #default_image;
    #circle;
    #width;
    #height;
    #font_size;
    #ConstructorSetDefaults(options, defaults) {
        return $.extend({}, defaults, options || {});
    }

    constructor(options)
    {
        if (!options.parent || !options.id)
        {
            console.error("InputPicture need a parent and an id!");
            return
        }
        
        let defaults = {
            text: "Change Image",
            default_image: "no-image.png",
            circle: true,
            width: "165px",
            height: "165px",
            font_size: "16px",
        }

        options = this.#ConstructorSetDefaults(options, defaults);

        this.#id = options.id;
        this.#text = options.text;
        this.#default_image = options.default_image;
        this.#circle = options.circle;     
        this.#width = options.width;   
        this.#height = options.height;
        this.#font_size = options.font_size;

        options.parent.append(`
        <form class="input-picture-form" method="post" enctype="multipart/form-data">
            <label class="input-picture-label" for="` + this.#id + `">
    	        <span class="input-picture-span">` + this.#text + `</span>
            </label>
            <input id="` + this.#id + `" type="file" name="` + this.#id + `">
            <img class="input-picture-image" src="` + this.#default_image + `"></img> 
        </form>
        `);
        this.UpdateCSS();
    }

    UpdateCSS() 
    {
        this.Get$Form().css({
            "color":"transparent",
            "transition":"all 0.3s ease",
            "display":"flex",
            "justify-content":"center",
            "align-items":"center",
            "position":"relative",
            "transition":"all 0.3s ease",
        })

        this.#UpdateLabel();
    
        this.Get$Input().css({
            "display":"none",
        })
        
        let border_radius;
        if (this.#circle)
            border_radius = "100px";
        else
            border_radius = "0px";

        this.#UpdateImage(border_radius);
        this.#UpdateHover(border_radius);

        this.Get$Span().css({
            "display":"inline-flex",
            "padding":"0.2em",
            "height":"2em",
        });
    }

    Get$Form()
    {
        return this.Get$Input().parent();
    }

    Get$Input()
    {
        return $("#" + this.#id);
    }

    Get$Image()
    {
        return this.Get$Form().find("img");
    }

    Get$Label()
    {
        return this.Get$Form().find("label");
    }

    Get$Span()
    {
        return this.Get$Form().find("span");
    }

    SetText(text)
    {
        this.Get$Form().find("span").text(text);
    }

    SetDefaultImage(src)
    {
        this.#default_image = src;
    }

    SetImage(src)
    {
        this.Get$Image().attr("src", src);
    }

    RemoveImage()
    {
        this.SetImage(this.#default_image);
    }

    SetCircle()
    {
        this.#circle = true;
        this.#UpdateBorderRadius()
    }

    SetSquare()
    {
        this.#circle = false;
        this.#UpdateBorderRadius()
    }

    SetWidth(new_width)
    {
        this.#width = new_width;
        this.#UpdateImage();
        this.#UpdateLabel();
    }

    SetHeight(new_height)
    {
        this.#height = new_height;
        this.#UpdateImage();
        this.#UpdateLabel();
    }

    SetFontSize(new_font_size)
    {
        this.#font_size = new_font_size;
        this.#UpdateLabel();
    }

    OnChange(func)
    {
        this.Get$Input().on("change", function(event){
            func(URL.createObjectURL(event.target.files[0]));
        });
    }

    Upload(options)
    {
        if (!options.url)
            options.url = ""
        if (!options.success)
            options.success = function(){}
        if (!options.data)
            options.data = {}
        if (!options.headers)
            options.headers = {}
        let input = document.getElementById(this.#id);
        let file = input.files[0];
        if(file != undefined){
            let formData= new FormData();
            if(!!file.type.match(/image.*/)){
                formData.append("image", file);
                $.ajax({
                  url: options.url,
                  type: "POST",
                  headers: options.headers,
                  data: formData,
                  processData: false,
                  contentType: false,
                  success: options.success,
                });
                return true;
            }
        }
        return false;
    }

    #UpdateBorderRadius()
    {
        let border_radius;
        if (this.#circle)
            border_radius = "100px";
        else
            border_radius = "0px";
        this.Get$Image().css("border-radius", border_radius);
        this.#UpdateHover(border_radius)
    }

    #UpdateHover(border_radius)
    {
        let $this = this

        let css = {
            "background-color":"rgba(0, 0, 0, 0.8)",
            "z-index":"10000",
            "color":"#fafafa",
            "border-radius":border_radius,
            "margin-bottom":"0",
            "transition":"background-color 0.2s ease-in-out",
        };

        this.Get$Form().off("mouseenter mouseleave").hover(function()
        {
            $this.Get$Form().css(css);
            $this.Get$Label().css(css);
        }, function(){
            for (const property in css)
            {
                $this.Get$Form().css(property, "");
                $this.Get$Label().css(property, "");
            }
        })
    }

    #UpdateImage(border_radius="")
    {
        if (border_radius != "")
            this.Get$Image().css("border-radius", border_radius);

        this.Get$Image().css({
            "position":"absolute",
            "object-fit":"cover",
            "width":this.#width,
            "height":this.#height,
            "box-shadow":"0 0 10px 0 rgba(255, 255, 255, 0.35)",
            "z-index":"0",
        })
    }

    #UpdateLabel()
    {
        this.Get$Label().css({
            "font-size": this.#font_size,
            "cursor":"pointer",
            "height":this.#height,
            "width": this.#width,
            "justify-content":"center",
            "align-items":"center",
            "display":"flex",
        })
    }
}

jQuery.fn.extend({
    inputPicture: function (id="")
    {
        let inputPicture = $(this).data("input-picture")
        if (inputPicture)
            return inputPicture;
        
        if (id == "" || id == undefined)
        {
            console.error("Input Picture must have an id")
            return undefined;
        }

        inputPicture = new InputPicture({
            parent: $(this),
            id: id,
        })
        $(this).data("input-picture", inputPicture)
        return inputPicture;
    }
})