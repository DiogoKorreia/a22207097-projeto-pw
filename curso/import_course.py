
from .models import (
    Course,
    Reason,
    Flat_plan,
    Subject,
)
import json
from django.db import transaction


with open('curso/json/lei.json') as f:
    course_info = json.load(f)


with transaction.atomic():

    for element, data in course_info.items():
        if element == "reasons":
            # Create 'Reason' objects
            for reason_data in data:
                Reason.objects.create(
                    text=reason_data['reason'],
                    order=reason_data['order']
                )

        elif element == "courseFlatPlan":

            flat_plan = Flat_plan.objects.create(years=3)


            for flatPlan_data in data:


                subject = Subject.objects.create(
                    name=flatPlan_data['curricularUnitName'],
                    year=flatPlan_data['curricularYear'],
                    semester=flatPlan_data['semesterCode'],
                    ects=flatPlan_data['ects'],
                    curricularIUnitReadableCode=flatPlan_data['curricularIUnitReadableCode'],
                )

                flat_plan.subjects.add(subject)

        elif element == "courseDetail":

                    course = Course.objects.create(
                        access_conditions=data.get("accessContidions", ""),
                        career_opportunities=data.get("careerOportunities", ""),
                        competences=data.get("competences", ""),
                        direction_contact=data.get("directionContact", ""),
                        direction_email=data.get("directionEmail", ""),
                        course_ects=data.get("courseECTS", 0),
                        course_name=data.get("courseName", ""),
                        course_secretariat_contact=data.get("courseSecretariatContact", ""),
                        course_secretariat_email=data.get("courseSecretariatEmail", ""),
                        future_studies=data.get("futureStudies", ""),
                        infrastructure=data.get("infrastructure", ""),
                        objectives=data.get("objectives", ""),
                        presentation=data.get("presentation", ""),
                        scientific_area=data.get("scientificArea", ""),
                        semesters=data.get("semesters", 0),
                        recipients=data.get("recipients", ""),
                        guest_teachers=data.get("guestTeachers", ""),
                    )
