# Define a dictionary of common sales objections and responses
objections = {
    "it's too expensive": "Our product may seem expensive, but it provides excellent value over time.",
    "i need to think about it": "Of course, take all the time you need. But keep in mind that our product is in high demand and stock may run out soon.",
    "i'm not interested": "That's perfectly fine, but can you tell me what specifically doesn't interest you about our product?",
    "i don't have time": "I understand that you're busy, but our product can save you a lot of time in the long run."
}

# Print out the list of objections
print("Here are some common objections:")
for objection in objections:
    print("- " + objection)

# Get the objection from the user and convert to lowercase
objection = input("What is the prospect's objection? ").lower()

# Respond to the objection
if objection in objections:
    print(objections[objection])
else:
    print("I'm sorry, I don't have a response for that objection.")
