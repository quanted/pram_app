"""
.. module:: terrplant_history
   :synopsis: Handles different versions of model to show correct view for a model object.
"""


def modelHistoryByVersion(model_obj):
    """
    Example method to return model object as HTML string 
    formatted by tables module. In practice, this method 
    should check model version to determine how to format 
    the model inputs and outputs.

    """
    import terrplant_tables
    modelOutputHTML = terrplant_tables.timestamp(model_obj)
    tables_output = terrplant_tables.table_all(model_obj)

    modelOutputHTML = modelOutputHTML + tables_output

    return modelOutputHTML