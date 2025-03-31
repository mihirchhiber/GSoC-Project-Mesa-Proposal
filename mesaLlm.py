from mesa import Agent, Model
import random
from mesa.space import MultiGrid
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

# Initialize LLM
llm = OllamaLLM(model="llama3.2", num_predict=1)

# Agent class with Personality
class LLMAgent(Agent):
    def __init__(self, unique_id, model, personality):
        # Correct initialization of Agent, with the model being passed as the first argument.
        super().__init__(model)  # Pass unique_id first and then model to the Agent base class
        self.llm = llm  # Access the LLM instance
        self.personality = personality  # Personality affects decision-making
        self.stock_held = 3  # Start with no stock holdings
        self.money_held = 70

    def make_decision(self, context):
        context = context.invoke({"amount" :self.stock_held, "personality": self.personality, "money": self.money_held})
        response = self.llm.invoke(context)
        decision = str(response)
        return decision

    def buy_stock(self, amount, banana_price):
        if self.money_held >= banana_price*amount:
            self.stock_held += amount
            self.money_held -= banana_price*amount
            print(f"Agent {self.unique_id} bought {amount} of Banana stock.")
        else:
            print(f"Agent {self.unique_id} could not buy {amount} of Banana stock.")
        

    def sell_stock(self, amount, banana_price):
        if self.stock_held >= amount:
            self.stock_held -= amount
            self.money_held += banana_price*amount
            print(f"Agent {self.unique_id} sold {amount} of Banana stock.")
        else:
            print(f"Agent {self.unique_id} tried to sell more than they own.")

    def hold_stock(self):
        print(f"Agent {self.unique_id} decided to hold their Banana stock.")

    
    def status(self, banana_price):
        print(f"""Agent {self.unique_id}
Personality: {self.personality}
Stocks: {self.stock_held}
Money: {self.money_held} 
Portfolio value: {self.money_held+self.stock_held*banana_price}
              """)


# Model class with Stock Pricing
class LLMModel(Model):
    def __init__(self, width, height, n, initial_prices=[9.5, 9.8, 10, 10.4, 10.1]):
        super().__init__()
        self.num_agents = n
        self.grid = MultiGrid(width, height, True)
        self.banana_price = initial_prices  # Initial price of the "banana" stock
        self.buy_count = 0  # Track the number of buys
        self.sell_count = 0  # Track the number of sells

        # Create agents with different personalities
        personalities = ["Aggressive", "Cautious", "Risk-Averse", "Optimistic", "Pessimistic"]
        agents = [LLMAgent(i, self, random.choice(personalities)) for i in range(self.num_agents)]
        x = self.rng.integers(0, self.grid.width, size=(n,))
        y = self.rng.integers(0, self.grid.height, size=(n,))
        
        for a, i, j in zip(agents, x, y):
            # Add the agent to a random grid cell
            self.grid.place_agent(a, (i, j))

    def calculate_stock_price(self):
        # Simple supply-demand model for stock price
        price_change = (self.buy_count - self.sell_count) * 0.1  # Small price fluctuation based on buy/sell activity
        new_price = self.banana_price[-1] + price_change + random.uniform(-3.0, 3.0)
        self.banana_price.append(max(1, new_price))  # Ensure the price doesn't go below 1
        print(f"New Banana stock price: {self.banana_price[-1]}")

    def step(self):
        self.buy_count = 0
        self.sell_count = 0
        
        context = """
The Banana pricing in the past has been: """ + str(self.banana_price[:-1]) + """"
The current price of Banana stock is $""" + str(self.banana_price[-1]) + """"
You have the following options:
1) Buy 1 Banana stock.
2) Buy 3 Banana stock.
3) Buy 5 Banana stock.
4) Sell 1 Banana stock.
5) Sell 3 Banana stock.
6) Sell 5 Banana stock.
7) Hold your position.

Make your decision. Be mindful of your personality and the current banana pricing. Start your response with the number of the option chosen. You currently hold {amount} banana stocks and you have ${money}.
Response no.: 
"""
        
        messages = [
            ("system", "You are a stock trader who is trading banana stock. Your personality type is {personality}"),
            ("human", context)
        ]

        prompt_template = ChatPromptTemplate.from_messages(messages)

        # Agents decide on their actions
        for agent in self.agents:
            decision = agent.make_decision(prompt_template)
            if "1" in decision.lower():
                agent.buy_stock(1, self.banana_price[-1])
                self.buy_count += 1
            elif "2" in decision.lower():
                agent.buy_stock(3, self.banana_price[-1])
                self.buy_count += 3
            elif "3" in decision.lower():
                agent.buy_stock(5, self.banana_price[-1])
                self.buy_count += 5
            elif "4" in decision.lower():
                agent.sell_stock(1, self.banana_price[-1])
                self.sell_count += 1
            elif "5" in decision.lower():
                agent.sell_stock(3, self.banana_price[-1])
                self.sell_count += 3
            elif "6" in decision.lower():
                agent.sell_stock(5, self.banana_price[-1])
                self.sell_count += 5
            else:
                agent.hold_stock()

        # Update the stock price after all actions
        self.calculate_stock_price()

    def status(self):

        for agent in self.agents:
            agent.status(self.banana_price[-1])

# Run the model
def run_model():
    model = LLMModel(10, 10, 20)
    for i in range(40):
        print(f"Step {i+1}")
        model.step()
    model.status()

if __name__ == "__main__":
    run_model()