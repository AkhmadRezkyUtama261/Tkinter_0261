flowers = ["🌸", "🌼", "🌺", "🌻", "🌷", "💐", "🌹", "🥀"]
        for _ in range(50):  # 50 bunga untuk kesan penuh
            x = random.randint(0, 600)
            y = random.randint(0, 800)
            flower = random.choice(flowers)
            self.canvas.create_text(x, y, text=flower, font=("Arial", 20), fill="#FFB6C1")