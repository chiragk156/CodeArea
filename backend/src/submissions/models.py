from django.db import models

from problems.models import Problem
from accounts.models import Profile
from contests.models import ContestsHaveProblems
# Create your models here.

class Submission(models.Model):
	""" Submissions to Normal Problems """

	ACCEPTED_ANSWER = 'AC'
	WRONG_ANSWER = 'WA'
	RUNTIME_ERROR = 'RE'
	TIME_EXCEEDED = 'TLE'
	INTERNAL_ERROR = 'IE'
	RUNNING = 'R'

	STATUS_CHOICES = (
		(ACCEPTED_ANSWER, 'ACCEPTED'),
		(WRONG_ANSWER, 'WRONG ANSWER'),
		(RUNTIME_ERROR, 'RUNTIME ERROR'),
		(TIME_EXCEEDED, 'TIME LIMIT EXCEEDED'),
		(INTERNAL_ERROR, 'INTERNAL ERROR'),
		(RUNNING, 'RUNNING')
	)

	user = models.ForeignKey(Profile, on_delete = models.CASCADE)
	problem = models.ForeignKey(Problem, on_delete = models.CASCADE)
	code = models.TextField()
	language = models.ForeignKey(Language, blank=True, null=True, on_delete = models.SET_NULL)
	status = models.CharField(max_length=3, choices= STATUS_CHOICES, default = RUNNING)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)


class ContestSubmission(models.Model):
	""" Submissions to Contest Problems """

	ACCEPTED_ANSWER = 'AC'
	WRONG_ANSWER = 'WA'
	RUNTIME_ERROR = 'RE'
	TIME_EXCEEDED = 'TLE'
	INTERNAL_ERROR = 'IE'
	RUNNING = 'R'

	STATUS_CHOICES = (
		(ACCEPTED_ANSWER, 'ACCEPTED'),
		(WRONG_ANSWER, 'WRONG ANSWER'),
		(RUNTIME_ERROR, 'RUNTIME ERROR'),
		(TIME_EXCEEDED, 'TIME LIMIT EXCEEDED'),
		(INTERNAL_ERROR, 'INTERNAL ERROR'),
		(RUNNING, 'RUNNING')
	)

	user = models.ForeignKey(Profile, on_delete = models.CASCADE)
	problem = models.ForeignKey(ContestsHaveProblems, on_delete = models.CASCADE)
	code = models.TextField()
	language = models.ForeignKey(Language, blank=True, null=True, on_delete = models.SET_NULL)
	status = models.CharField(max_length=3, choices= STATUS_CHOICES, default = RUNNING)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)


class Language(models.Model):
	""" Language used """
	language_name = models.CharField(max_length=100)