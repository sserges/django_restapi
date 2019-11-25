import json

from django.views.generic import View
from django.http import HttpResponse

from updates.forms import UpdateModelForm
from updates.models import Update as UpdateModel
from cfeapi.mixins import HttpResponseMixin
from .mixins import CSRFExemptMixin
from .utils import is_json

# Creating, Updating, Deleting, Retrieving (1) -- Update Model


class UpdateModelDetailAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    """
    Retrieve, Update, Delete --> Object
    """

    is_json = True

    def get_object(self, id=None):
        # try:
        #     obj = UpdateModel.objects.get(id=id)
        # except UpdateModel.DoesNotExist:
        #     obj = None
        """
        Below handles a Does Not Exist Exception too
        """
        qs = UpdateModel.objects.filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def get(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=404)

        json_data = obj.serialize()
        return self.render_to_response(json_data)
    
    def post(self, request, *args, **kwargs):
        json_data  = json.dumps({"message": "Not allowed, please use the /api/updates/ endpoint"})
        return self.render_to_response(json_data, status=403)
    
    def put(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=404)
        # print(request.POST)
        print(request.body)

        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({"message": "Invalid data sent, please send using JSON."})
            return self.render_to_response(error_data, status=400)

        new_data = json.loads(request.body)
        print(new_data['content'])
        json_data  = json.dumps({})
        return self.render_to_response(json_data)
    
    def delete(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=404)
        json_data  = {}
        return self.render_to_response(json_data, status=403)


class UpdateModelListAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    """
    List View
    Create View
    """

    is_json = True
   

    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return self.render_to_response(json_data)
    
    def post(self, request, *args, **kwargs):
        # print(request.POST)
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({"message": "Invalid data sent, please send using JSON."})
            return self.render_to_response(error_data, status=400)
        data = json.loads(request.body)
        form = UpdateModelForm(data)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        data = json.dumps({"message": "Not Allowed"})
        return self.render_to_response(data, status=400)
    
    def delete(self, request, *args, **kwargs):
        data = json.dumps({"message": "You cannot delete an entire list"})
        return self.render_to_response(data, status=403)