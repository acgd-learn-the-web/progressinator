from django.urls import path
from progressinator.core.views import auth, grades, profile, api, teachers


app_name = 'core'

urlpatterns = [
    path('', grades.courses, name='courses'),
    path('courses/<slug:course_id>/', grades.course_grades, name='grades'),
    path('auth/sign-in/', auth.signin, name='sign_in'),
    path('auth/sign-out/', auth.signout, name='sign_out'),
    path('profile/', profile.index, name='profile'),
    path('profile/save/', profile.save, name='profile_save'),
    path('teachers/courses/', teachers.courses, name='teacher_courses'),
    path('teachers/courses/<slug:term_id>/<slug:course_id>/', teachers.course_status, name='teacher_course'),
    path('teachers/courses/<slug:term_id>/<slug:course_id>/download/<slug:student_grade_group>/', teachers.download, name='teacher_download'),
    path('teachers/courses/<slug:term_id>/<slug:course_id>/users/<int:user_id>/', teachers.user_grades, name='teacher_user_grades'),
    path('teachers/courses/<slug:term_id>/<slug:course_id>/users/<int:user_id>/save/', teachers.user_grades_save, name='teacher_user_grades_save'),
    path('teachers/courses/<slug:term_id>/<slug:course_id>/assessments/<str:assessment_id>/', teachers.assessment_grades, name='teacher_assessment_grades'),
    path('teachers/courses/<slug:term_id>/<slug:course_id>/assessments/<str:assessment_id>/save/', teachers.assessment_grades_save, name='teacher_assessment_grades_save'),
    path('api/v1/courses/<slug:term_id>/<slug:course_id>/users/<int:user_id>/download/', api.user_grades_download, name='user_grades_download'),
    path('api/v1/submit-assessment', api.submit_assessment, name='submit'),
]
