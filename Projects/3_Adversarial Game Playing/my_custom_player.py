
from sample_players import DataPlayer
import random
from functools import reduce
from itertools import chain
        

class AlphaBetaPlayer(DataPlayer):
    
    def get_action(self, state):
        if state.ply_count == 1:
            self.queue.put(57) # random.choice(state.actions()))
        elif state.ply_count == 0:
            self.queue.put(58) # random.choice(state.actions()))
        else:
            self.queue.put(self.alpha_beta_search(state, depth=3))

    def alpha_beta_search(self, state, depth):

        def min_value(state, alpha, beta, depth):
            if state.terminal_test(): return state.utility(self.player_id)
            if depth <= 0: return self.score(state)
            value = float("inf")
            for action in state.actions():
                value = min(value, max_value(state.result(action), alpha, beta, depth-1))
                if value <= alpha:
                    return value
                beta = min(beta, value)
            return value

        def max_value(state, alpha, beta, depth):
            if state.terminal_test(): return state.utility(self.player_id)
            if depth <= 0: return self.score(state)
            value = float("-inf")
            for action in state.actions():
                value = max(value, min_value(state.result(action), alpha, beta, depth-1))
                if value >= beta:
                    alpha = max(alpha, value)
            return value

        def get_move(best_options, next_action):
            (best_move, best_score, alpha) = best_options
            value = min_value(state.result(next_action), alpha, float("-inf"), depth-1)
            alpha = max(alpha, value)
            return (next_action, value, alpha) if value >= best_score else (best_move, best_score, alpha)

        return reduce(
            get_move,
            state.actions(),
            (None, float("-inf"), float("-inf"))
        )[0]

    def score(self, state):
        return self.score_liberties_of_liberties(state)
    
    def score_liberties_of_liberties(self, state):
        own_loc = state.locs[self.player_id]
        opp_loc = state.locs[1 - self.player_id]
        own_liberties = state.liberties(own_loc)
        opp_liberties = state.liberties(opp_loc)
        own_liberties2 = sum(len(state.liberties(l)) for l in own_liberties)
        opp_liberties2 = sum(len(state.liberties(l)) for l in opp_liberties)
            
        a = 1
        b = 2
        d1 = a * len(own_liberties) - b * len(opp_liberties)
        d2 = a * own_liberties2 - b * opp_liberties2
        
        return d1 + d2
        
    def score_liberties_of_liberties_collapse(self, state):
        own_loc = state.locs[self.player_id]
        opp_loc = state.locs[1 - self.player_id]
        own_liberties = set(state.liberties(own_loc))
        opp_liberties = set(state.liberties(opp_loc))
        collapse1 = own_liberties & opp_liberties
        
        a = 1
        b = 2
        
        score1 = a * len(own_liberties) + len(collapse1) - b * len(opp_liberties)
        
        own_liberties2 = set(chain(*[state.liberties(l) for l in own_liberties]))
        opp_liberties2 = set(chain(*[state.liberties(l) for l in opp_liberties]))
        collapse2 = own_liberties2 & opp_liberties2
        score2 = a * len(own_liberties2) + len(collapse2) - b * len(opp_liberties2)
        
        return score1 + score2
    
    def score_baseline(self, state):
        own_loc = state.locs[self.player_id]
        opp_loc = state.locs[1 - self.player_id]
        own_liberties = len(state.liberties(own_loc))
        opp_liberties = len(state.liberties(opp_loc))
        
        return own_liberties - opp_liberties
    
class CustomPlayer(AlphaBetaPlayer):
    """ Implement your own agent to play knight's Isolation

    The get_action() method is the only required method for this project.
    You can modify the interface for get_action by adding named parameters
    with default values, but the function MUST remain compatible with the
    default interface.

    **********************************************************************
    NOTES:
    - The test cases will NOT be run on a machine with GPU access, nor be
      suitable for using any other machine learning techniques.

    - You can pass state forward to your agent on the next turn by assigning
      any pickleable object to the self.context attribute.
    **********************************************************************
    """
#     def get_action(self, state):
#         """ Employ an adversarial search technique to choose an action
#         available in the current state calls self.queue.put(ACTION) at least

#         This method must call self.queue.put(ACTION) at least once, and may
#         call it as many times as you want; the caller will be responsible
#         for cutting off the function after the search time limit has expired.

#         See RandomPlayer and GreedyPlayer in sample_players for more examples.

#         **********************************************************************
#         NOTE: 
#         - The caller is responsible for cutting off search, so calling
#           get_action() from your own code will create an infinite loop!
#           Refer to (and use!) the Isolation.play() function to run games.
#         **********************************************************************
#         """
        # TODO: Replace the example implementation below with your own search
        #       method by combining techniques from lecture
        #
        # EXAMPLE: choose a random move without any search--this function MUST
        #          call self.queue.put(ACTION) at least once before time expires
        #          (the timer is automatically managed for you)

#         self.queue.put(random.choice(state.actions()))
        
        