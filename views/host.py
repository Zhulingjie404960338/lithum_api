from models import HostModel
from views import APIView


class HostView(APIView):
    def get(self):
        data = HostModel.get()
        return {"count": len(data), "list": data}

    def post(self):
        return {}

    def put(self):
        return {}

    def delete(self):
        return {}
