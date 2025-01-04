from typing import Dict, Any, List
import numpy as np
import sympy as sp
from dataclasses import dataclass

@dataclass
class MathProblem:
    question: str
    solution: str
    steps: List[str]
    variables: Dict[str, Any]

class MathEnvironment:
    """Environment for mathematical reasoning and problem-solving"""
    
    def __init__(self):
        self.history = []
        self.symbols = {}
        self.current_problem = None
        
    def set_problem(self, problem: MathProblem):
        """Set a new math problem to solve"""
        self.current_problem = problem
        self.history.append(problem)
        
    def verify_solution(self, proposed_solution: str) -> bool:
        """Verify if the proposed solution matches the correct solution"""
        if self.current_problem is None:
            return False
        return self.current_problem.solution.strip() == proposed_solution.strip()
    
    def evaluate_expression(self, expression: str) -> float:
        """Evaluate a mathematical expression"""
        try:
            return float(sp.sympify(expression).evalf())
        except:
            return None
    
    def step_by_step_solve(self, problem: MathProblem) -> List[str]:
        """Execute step-by-step problem solving"""
        self.set_problem(problem)
        return problem.steps
    
    def get_hint(self) -> str:
        """Get a hint for the current problem"""
        if self.current_problem is None:
            return "No problem is currently set."
        if len(self.current_problem.steps) > 0:
            return self.current_problem.steps[0]
        return "No hints available."
    
    def create_problem(self, question: str, solution: str, steps: List[str], variables: Dict[str, Any] = None) -> MathProblem:
        """Create a new math problem"""
        if variables is None:
            variables = {}
        return MathProblem(question=question, solution=solution, steps=steps, variables=variables)