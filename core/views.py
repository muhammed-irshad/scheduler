from datetime import datetime
from rest_framework import views, status, response
from .serializers import UserSerializer
from .models import User


class RegisterTime(views.APIView):
    def post(self, request, *args, **kwargs):
        from_time = request.data.get("from_time")
        to_time = request.data.get("to_time")

        from_time = datetime.strptime(from_time, "%I:%M %p").time()
        to_time = datetime.strptime(to_time, "%I:%M %p").time()

        user = User.objects.create(
            from_time=from_time, to_time=to_time
        )
        seriazlier = UserSerializer(instance=user)

        return response.Response(data=seriazlier.data)


class AvailableTimeSlots(views.APIView):
    def get(self, request, *args, **kwargs):
        interviewer_id = request.query_params.get("interviewer_id")
        candidate_id = request.query_params.get("candidate_id")

        interviewer = User.objects.filter(id=interviewer_id).first()
        candidate = User.objects.filter(id=candidate_id).first()

        if not interviewer or not candidate:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)

        # select max from start time and min from end time of both interviewer and candidate
        from_time = max([interviewer.from_time, candidate.from_time])
        to_time = min([interviewer.to_time, candidate.to_time])

        time_available = []
        for i in range(from_time.hour, to_time.hour, 1):
            time_available.append((i, i + 1))

        return response.Response({"Time avalailable": time_available})
