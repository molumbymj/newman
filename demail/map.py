import json
import tangelo
import cherrypy

from es_geo import es_get_sender_locations
from newman.newman_config import getDefaultDataSetID
from param_utils import parseParamDatetime, parseParamEmailIds, parseParamStarred, parseParamTextQuery

#GET /sender_locations/<id>?qs="<query string>"
# deprecated slated for removal
def sender_locations(*args, **kwargs):
    tangelo.log("getEmail(args: %s kwargs: %s)" % (str(args), str(kwargs)))
    tangelo.content_type("application/json")

    data_set_id, start_datetime, end_datetime, size = parseParamDatetime(**kwargs)

    qs = parseParamTextQuery(**kwargs)

    return es_get_sender_locations(data_set_id, size)

get_actions = {
    "sender_locations" : sender_locations
}

def unknown(*args):
    return tangelo.HTTPStatusCode(400, "invalid service call")

@tangelo.restful
def get(action, *args, **kwargs):

    cherrypy.log("map(args[%s] %s)" % (len(args), str(args)))
    cherrypy.log("map(kwargs[%s] %s)" % (len(kwargs), str(kwargs)))

    if ("data_set_id" not in kwargs) or (kwargs["data_set_id"] == "default_data_set"):
        kwargs["data_set_id"] = getDefaultDataSetID()

    return get_actions.get(action, unknown)( *args, **kwargs)