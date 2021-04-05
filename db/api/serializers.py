from rest_meets_djongo.serializers import DjongoModelSerializer

from api.models import Introduce, Projects, TechStack


class IntroduceSerializer(DjongoModelSerializer):
    class Meta:
        model = Introduce
        fields = '__all__'


class ProjectsSerializer(DjongoModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class TechStackSerializer(DjongoModelSerializer):
    class Meta:
        model = TechStack
        fields = '__all__'
