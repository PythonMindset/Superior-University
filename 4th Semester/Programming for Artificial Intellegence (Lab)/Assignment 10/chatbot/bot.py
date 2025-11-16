from nltk.chat.util import Chat, reflections

pairs = [
    [r"(?i).*hello.*|.*hi.*|.*hey.*",
     ["Hello! I'm your Study Planner Bot. How can I help you improve your productivity today?",
      "Hi there! Ready to boost your studies? Ask me for a study plan, motivation, or focus tips.",
      "Hey! I'm here to assist you with creating a productive study schedule."]],

    [r"(?i).*study plan.*|.*plan for today.*|.*schedule.*",
     ["Here’s a detailed study plan for today:\n"
      "9–11 AM: Focus on main subjects using the Pomodoro technique.\n"
      "11–11:15 AM: Short break, hydrate, stretch.\n"
      "11:15–1 PM: Practice exercises or assignments.\n"
      "1–2 PM: Lunch break.\n"
      "2–4 PM: Review lessons and summarize notes.\n"
      "4–5 PM: Plan tomorrow’s tasks and review progress.",
      "Today's study schedule:\n"
      "9–10:30 AM: Core subject study\n"
      "10:30–10:45 AM: Break\n"
      "10:45–12 PM: Practice problems\n"
      "12–1 PM: Review notes\n"
      "1–2 PM: Lunch\n"
      "2–4 PM: Secondary subjects or projects\n"
      "4–5 PM: Organize tasks for tomorrow"]],

    [r"(?i).*motivation.*|.*encourage.*|.*inspire.*",
     ["Remember: Consistency beats intensity. Keep moving forward, even in small steps!",
      "You are capable of amazing things. Start now, momentum will follow.",
      "Every study session counts. Take small actions and celebrate progress."]],

    [r"(?i).*focus.*|.*concentration.*|.*avoid distractions.*",
     ["To improve focus: try the Pomodoro technique, remove distractions, and take 5-min breaks.",
      "Focus tip: study in short intervals of 25–30 minutes and avoid multitasking.",
      "Eliminate distractions: silence notifications, keep your desk clean, and stay hydrated."]],

    [r"(?i).*break.*|.*relax.*|.*rest.*",
     ["Take a 10-minute break: stretch, drink water, and relax your eyes.",
      "Break tip: Walk around, grab a snack, and reset your mind before the next study session.",
      "Short breaks help maintain concentration. Try a quick meditation or breathing exercise."]],

    [r"(?i).*tasks.*|.*todo.*|.*assignments.*",
     ["List your tasks clearly and prioritize the most important ones first.",
      "Divide large assignments into smaller steps and schedule them across the day.",
      "Track your tasks and mark them complete. This helps stay motivated."]],

    [r"(?i).*sentiment.*|.*mood.*",
     ["You can tell me how you feel, and I can suggest motivation or relaxation tips."]],

    [r"(?i).*bye.*|.*goodbye.*|.*see you.*",
     ["Goodbye! Keep studying smartly and stay productive.",
      "See you later! Don’t forget to follow your study plan.",
      "Take care! Remember to take breaks and stay consistent."]]
]
chatbot=Chat(pairs, reflections)