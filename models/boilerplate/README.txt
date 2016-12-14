This is boilerplate code for creating a new model page within the "ubertool".

You can view this page at: <localhost:port>/ubertool/boilerplate


Steps to create a new model based off of this boilerplate:

    1) Copy this folder ("qed/ubertool_eco/modesl/boilerplate") and rename it to the new desired model name.
        e.g. qed/ubertool_eco/modesl/pices
    2) Now you have to rename everywhere that says "boilplate" in the code to your new model name (e.g. "pices")
        Note: there are a few occurrences of "Boilplate" (capitalized). This is important. So if you do a
        "find and replace" approach, make sure its case sensitive
            e.g. "BoilplateInp" in the "boilerplate_parameters.py"
    3) All occurrences of the model name in the code are "magic strings" and need to be formatted exact to work



Input Page:

    The "<model>_input.py" controls what is shown at: /ubertool/<model>/input

    If you want to follow the "ubertool" template that uses a model input form and an "output" page,
    then you can copy the "<model>_input.py" from a similar model.
        Note: models with "tabbed" input pages are done differently than non-tabbed models

    If you want a custom input page (e.g. pices), then you have to adapt the "<model>_input.py" to suit your needs.
        Things to consider when taking this approach:

            1) The "<model>_input.py" represents only a portion of whole "Input" page. "/views/input.py" renders the
                whole input page, calling "<model>_input.py" to fill in the area to the right of "links left" and
                above the footer.
            2) Because of this, you are limited to a certain number of pixels (space between links left and the far
                right border)
            3) If you want/need more horizontal pixels, then you are going to have to make an exception for your model
                in "/views/input.py" to render differently. Do that at your own risk.
            4) Unfortunately, this is a restriction of the current ubertool design. A new design could easily get rid
                of this restraint, but would require significant code changes.


If you need to use a tables.py for the output page of the model, follow these steps:

    1) Add new model to "outputs.py" so ""<model>_tables.py" will render correctly upon successful model run
        - Add the model name to the "_UPDATED_MODELS" tuple in "/views/outputs.py"
    2) Update the "<model>_tables.py" to match the input and output keys returned from a model run
        - look at another similar model to learn how to do this as its outside the scope of this text