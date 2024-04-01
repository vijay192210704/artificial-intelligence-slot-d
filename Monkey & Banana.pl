on_floor(monkey).
on_floor(chair).
on_ceiling(banana).

% Rules representing possible actions
climb(monkey, chair) :-
    on_floor(monkey),
    on_floor(chair).

push(chair, banana) :-
    on_floor(chair),
    on_ceiling(banana).

% Rules representing the possible states after an action
state_after(Action, State) :-
    state_before(StateBefore),
    call(Action, StateBefore, State).

% Rule to represent the starting state
state_before([on_floor(monkey), on_floor(chair), on_ceiling(banana)]).

goal_state([on_monkey(banana)]).

is_goal(State) :-
    goal_state(Goal),
    subset(Goal, State).

move_toward_goal(State, Actions) :-
    state_after(Action, State),
    is_goal(State),
    Actions = [Action].

move_toward_goal(State, Actions) :-
    state_after(Action, State),
    \+ is_goal(State),
    move_toward_goal(State, RestActions),
    Actions = [Action | RestActions].

subset([], _).
subset([H|T], List) :-
    member(H, List),
    subset(T, List).