symptom(john, fever).
symptom(johnny, cough).
symptom(mary, headache).
symptom(gennie, fatigue).
symptom(bob, cough).
symptom(beyers, fatigue).

disease(fever, cold).
disease(cough, cold).
disease(fever, flue).
disease(cough, flue).
disease(headache, flue).
disease(fatigue, flue).

get_report(Patient, Symptom, Disease) :-
    symptom(Patient, Symptom),
	disease(Symptom, Disease).
  
   