import tkinter as tk
from tkinter import ttk, messagebox
import math

class VexineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vexine - Your Personal Health Guide")
    
        # FULLSCREEN - Choose one method below
    
        # Method 1: True Fullscreen (recommended for immersive experience)
        self.root.attributes('-fullscreen', True)
        self.root.bind('<Escape>', lambda e: self.root.attributes('-fullscreen', False))
        self.root.bind('<F11>', lambda e: self.root.attributes('-fullscreen', 
                    not self.root.attributes('-fullscreen')))
    
        # Method 2: Maximized (uncomment if you prefer this over fullscreen)
        # self.root.state('zoomed')  # Windows/Linux
    
        # Method 3: 90% of screen, centered (uncomment if you prefer this)
        # screen_width = self.root.winfo_screenwidth()
        # screen_height = self.root.winfo_screenheight()
        # width = int(screen_width * 0.9)
        # height = int(screen_height * 0.9)
        # x = (screen_width - width) // 2
        # y = (screen_height - height) // 2
        # self.root.geometry(f"{width}x{height}+{x}+{y}")
    
        # Color scheme - professional with casual mix
        self.colors = {
            'primary': '#2C3E50',
            'secondary': '#3498DB',
            'accent': '#E74C3C',
            'success': '#27AE60',
            'bg': '#ECF0F1',
            'card': '#FFFFFF',
            'text': '#2C3E50',
            'light_text': '#7F8C8D'
        }
    
        # Configure root background
        self.root.configure(bg=self.colors['bg'])
    
        # Initialize variables
        self.age = tk.IntVar(value=25)
        self.gender = tk.StringVar(value="male")
        self.height_cm = tk.DoubleVar(value=170.0)
        self.weight_kg = tk.DoubleVar(value=70.0)
        self.current_body_type = tk.StringVar(value="average")
        self.desired_body_type = tk.StringVar(value="athletic")
        self.fitness_level = tk.StringVar(value="beginner")
        self.goal = tk.StringVar(value="maintain")

        # BMI result variables
        self.bmi_value = tk.StringVar(value="--")
        self.bmi_category = tk.StringVar(value="Calculate to see results")
        self.ideal_weight_range = tk.StringVar(value="--")
    
        # Build UI
        self.create_header()
        self.create_main_content()

        
    def create_header(self):
        """Create application header"""
        header_frame = tk.Frame(self.root, bg=self.colors['primary'], height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        # App title
        title = tk.Label(
            header_frame,
            text="VEXINE",
            font=('Helvetica', 28, 'bold'),
            bg=self.colors['primary'],
            fg='white'
        )
        title.pack(side=tk.LEFT, padx=30, pady=20)
        
        # Subtitle
        subtitle = tk.Label(
            header_frame,
            text="Your Personal Health & Fitness Guide",
            font=('Helvetica', 12),
            bg=self.colors['primary'],
            fg=self.colors['bg']
        )
        subtitle.pack(side=tk.LEFT, padx=(0, 20), pady=20)
        
    def create_main_content(self):
        """Create main content area with scrollable frame"""
        # Main container
        main_container = tk.Frame(self.root, bg=self.colors['bg'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create two-column layout
        left_column = tk.Frame(main_container, bg=self.colors['bg'])
        left_column.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        right_column = tk.Frame(main_container, bg=self.colors['bg'])
        right_column.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        # Left column content
        self.create_input_section(left_column)
        self.create_body_type_section(left_column)
        
        # Right column content
        self.create_results_section(right_column)
        self.create_recommendations_section(right_column)
        
    def create_card_frame(self, parent, title):
        """Create a styled card frame"""
        card = tk.Frame(parent, bg=self.colors['card'], relief=tk.RAISED, bd=2)
        card.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        # Card title
        title_frame = tk.Frame(card, bg=self.colors['secondary'], height=40)
        title_frame.pack(fill=tk.X)
        title_frame.pack_propagate(False)
        
        tk.Label(
            title_frame,
            text=title,
            font=('Helvetica', 14, 'bold'),
            bg=self.colors['secondary'],
            fg='white'
        ).pack(side=tk.LEFT, padx=15, pady=8)
        
        # Content frame
        content = tk.Frame(card, bg=self.colors['card'])
        content.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        return content
        
    def create_input_section(self, parent):
        """Create basic input section"""
        content = self.create_card_frame(parent, "📊 Basic Information")
        
        # Age
        self.create_labeled_spinbox(content, "Age (years):", self.age, 10, 100, row=0)
        
        # Gender
        gender_frame = tk.Frame(content, bg=self.colors['card'])
        gender_frame.grid(row=1, column=0, columnspan=2, sticky='w', pady=8)
        
        tk.Label(
            gender_frame,
            text="Gender:",
            font=('Helvetica', 11),
            bg=self.colors['card'],
            fg=self.colors['text']
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        tk.Radiobutton(
            gender_frame,
            text="Male",
            variable=self.gender,
            value="male",
            font=('Helvetica', 10),
            bg=self.colors['card'],
            fg=self.colors['text'],
            activebackground=self.colors['card'],
            selectcolor=self.colors['card']
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Radiobutton(
            gender_frame,
            text="Female",
            variable=self.gender,
            value="female",
            font=('Helvetica', 10),
            bg=self.colors['card'],
            fg=self.colors['text'],
            activebackground=self.colors['card'],
            selectcolor=self.colors['card']
        ).pack(side=tk.LEFT, padx=5)
        
        # Height
        self.create_labeled_spinbox(content, "Height (cm):", self.height_cm, 100, 250, row=2, increment=0.5)
        
        # Weight
        self.create_labeled_spinbox(content, "Weight (kg):", self.weight_kg, 30, 200, row=3, increment=0.5)
        
        # Fitness Level
        tk.Label(
            content,
            text="Fitness Level:",
            font=('Helvetica', 11),
            bg=self.colors['card'],
            fg=self.colors['text']
        ).grid(row=4, column=0, sticky='w', pady=8)
        
        fitness_combo = ttk.Combobox(
            content,
            textvariable=self.fitness_level,
            values=["beginner", "intermediate", "advanced"],
            state='readonly',
            width=18,
            font=('Helvetica', 10)
        )
        fitness_combo.grid(row=4, column=1, sticky='w', pady=8)
        
        # Calculate button
        calc_btn = tk.Button(
            content,
            text="Calculate BMI & Get Recommendations",
            font=('Helvetica', 12, 'bold'),
            bg=self.colors['success'],
            fg='white',
            activebackground='#229954',
            activeforeground='white',
            cursor='hand2',
            relief=tk.FLAT,
            padx=20,
            pady=10,
            command=self.calculate_bmi
        )
        calc_btn.grid(row=5, column=0, columnspan=2, pady=(15, 5))
        
    def create_labeled_spinbox(self, parent, label_text, variable, from_, to, row, increment=1):
        """Create a labeled spinbox"""
        tk.Label(
            parent,
            text=label_text,
            font=('Helvetica', 11),
            bg=self.colors['card'],
            fg=self.colors['text']
        ).grid(row=row, column=0, sticky='w', pady=8)
        
        spinbox = tk.Spinbox(
            parent,
            from_=from_,
            to=to,
            textvariable=variable,
            width=20,
            font=('Helvetica', 10),
            increment=increment
        )
        spinbox.grid(row=row, column=1, sticky='w', pady=8)
        
    def create_body_type_section(self, parent):
        """Create body type selection section"""
        content = self.create_card_frame(parent, "🎯 Body Type & Goals")
        
        # Current body type
        tk.Label(
            content,
            text="Current Body Type:",
            font=('Helvetica', 11),
            bg=self.colors['card'],
            fg=self.colors['text']
        ).grid(row=0, column=0, sticky='w', pady=8)
        
        current_combo = ttk.Combobox(
            content,
            textvariable=self.current_body_type,
            values=["underweight", "average", "athletic", "overweight", "obese"],
            state='readonly',
            width=18,
            font=('Helvetica', 10)
        )
        current_combo.grid(row=0, column=1, sticky='w', pady=8)
        
        # Desired body type
        tk.Label(
            content,
            text="Desired Body Type:",
            font=('Helvetica', 11),
            bg=self.colors['card'],
            fg=self.colors['text']
        ).grid(row=1, column=0, sticky='w', pady=8)
        
        desired_combo = ttk.Combobox(
            content,
            textvariable=self.desired_body_type,
            values=["lean", "athletic", "muscular", "maintain current"],
            state='readonly',
            width=18,
            font=('Helvetica', 10)
        )
        desired_combo.grid(row=1, column=1, sticky='w', pady=8)
        
        # Goal
        tk.Label(
            content,
            text="Primary Goal:",
            font=('Helvetica', 11),
            bg=self.colors['card'],
            fg=self.colors['text']
        ).grid(row=2, column=0, sticky='w', pady=8)
        
        goal_combo = ttk.Combobox(
            content,
            textvariable=self.goal,
            values=["lose weight", "gain muscle", "maintain", "improve fitness"],
            state='readonly',
            width=18,
            font=('Helvetica', 10)
        )
        goal_combo.grid(row=2, column=1, sticky='w', pady=8)
        
    def create_results_section(self, parent):
        """Create BMI results display section"""
        content = self.create_card_frame(parent, "📈 Your BMI Results")
        
        # BMI Value display
        bmi_display_frame = tk.Frame(content, bg=self.colors['bg'], relief=tk.SUNKEN, bd=2)
        bmi_display_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(
            bmi_display_frame,
            text="BMI:",
            font=('Helvetica', 14),
            bg=self.colors['bg'],
            fg=self.colors['text']
        ).pack(pady=(10, 0))
        
        tk.Label(
            bmi_display_frame,
            textvariable=self.bmi_value,
            font=('Helvetica', 32, 'bold'),
            bg=self.colors['bg'],
            fg=self.colors['secondary']
        ).pack()
        
        tk.Label(
            bmi_display_frame,
            textvariable=self.bmi_category,
            font=('Helvetica', 12, 'italic'),
            bg=self.colors['bg'],
            fg=self.colors['light_text']
        ).pack(pady=(0, 10))
        
        # Ideal weight range
        tk.Label(
            content,
            text="Ideal Weight Range:",
            font=('Helvetica', 11, 'bold'),
            bg=self.colors['card'],
            fg=self.colors['text']
        ).pack(anchor='w', pady=(10, 5))
        
        tk.Label(
            content,
            textvariable=self.ideal_weight_range,
            font=('Helvetica', 11),
            bg=self.colors['card'],
            fg=self.colors['text']
        ).pack(anchor='w')
        
        # BMI Categories reference
        categories_frame = tk.LabelFrame(
            content,
            text="BMI Categories",
            font=('Helvetica', 10, 'bold'),
            bg=self.colors['card'],
            fg=self.colors['text']
        )
        categories_frame.pack(fill=tk.X, pady=(15, 0))
        
        categories = [
            ("< 18.5", "Underweight", "#3498DB"),
            ("18.5 - 24.9", "Normal", "#27AE60"),
            ("25.0 - 29.9", "Overweight", "#F39C12"),
            ("≥ 30.0", "Obese", "#E74C3C")
        ]
        
        for bmi_range, category, color in categories:
            cat_frame = tk.Frame(categories_frame, bg=self.colors['card'])
            cat_frame.pack(fill=tk.X, padx=10, pady=2)
            
            tk.Label(
                cat_frame,
                text="●",
                font=('Helvetica', 16),
                bg=self.colors['card'],
                fg=color
            ).pack(side=tk.LEFT)
            
            tk.Label(
                cat_frame,
                text=f"{bmi_range}: {category}",
                font=('Helvetica', 9),
                bg=self.colors['card'],
                fg=self.colors['text']
            ).pack(side=tk.LEFT, padx=5)
        
    def create_recommendations_section(self, parent):
        """Create recommendations display section"""
        content = self.create_card_frame(parent, "💡 Personalized Recommendations")
        
        # Create text widget with scrollbar
        text_frame = tk.Frame(content, bg=self.colors['card'])
        text_frame.pack(fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.recommendations_text = tk.Text(
            text_frame,
            wrap=tk.WORD,
            width=40,
            height=20,
            font=('Helvetica', 10),
            bg=self.colors['bg'],
            fg=self.colors['text'],
            yscrollcommand=scrollbar.set,
            relief=tk.FLAT,
            padx=10,
            pady=10,
            state=tk.NORMAL
        )
        self.recommendations_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.recommendations_text.yview)
        
        # Configure text tags for styling
        self.recommendations_text.tag_config('heading', font=('Helvetica', 12, 'bold'), foreground=self.colors['secondary'])
        self.recommendations_text.tag_config('subheading', font=('Helvetica', 10, 'bold'), foreground=self.colors['primary'])
        self.recommendations_text.tag_config('bullet', foreground=self.colors['success'])
        
        # Initial message
        self.recommendations_text.insert('1.0', "Click 'Calculate BMI & Get Recommendations' to see your personalized health and fitness plan!")
        self.recommendations_text.config(state=tk.DISABLED)
        
    def calculate_bmi(self):
        """Calculate BMI and generate recommendations"""
        try:
            # Get values
            height_m = self.height_cm.get() / 100
            weight = self.weight_kg.get()
            
            # Validate inputs
            if height_m <= 0 or weight <= 0:
                messagebox.showerror("Invalid Input", "Height and weight must be positive values!")
                return
            
            # Calculate BMI
            bmi = weight / (height_m ** 2)
            self.bmi_value.set(f"{bmi:.1f}")
            
            # Determine category
            if bmi < 18.5:
                category = "Underweight"
                color = "#3498DB"
            elif 18.5 <= bmi < 25:
                category = "Normal Weight"
                color = "#27AE60"
            elif 25 <= bmi < 30:
                category = "Overweight"
                color = "#F39C12"
            else:
                category = "Obese"
                color = "#E74C3C"
            
            self.bmi_category.set(category)
            
            # Calculate ideal weight range (BMI 18.5 - 24.9)
            ideal_min = 18.5 * (height_m ** 2)
            ideal_max = 24.9 * (height_m ** 2)
            self.ideal_weight_range.set(f"{ideal_min:.1f} - {ideal_max:.1f} kg")
            
            # Generate recommendations
            self.generate_recommendations(bmi, category, weight, ideal_min, ideal_max)
            
        except tk.TclError:
            messagebox.showerror("Invalid Input", "Please enter valid numerical values!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def generate_recommendations(self, bmi, category, current_weight, ideal_min, ideal_max):
        """Generate personalized nutrition and exercise recommendations"""
        # Enable text widget
        self.recommendations_text.config(state=tk.NORMAL)
        
        # Clear existing content
        self.recommendations_text.delete('1.0', tk.END)
        
        # Build recommendations as a single string
        recommendations = "YOUR PERSONALIZED PLAN\n\n"
        
        # BMI Analysis
        recommendations += "📊 BMI Analysis\n"
        if bmi < 18.5:
            recommendations += f"Your BMI indicates you're underweight. Target: gain {ideal_min - current_weight:.1f} kg to reach healthy range.\n\n"
        elif bmi >= 30:
            recommendations += f"Your BMI indicates obesity. Target: lose {current_weight - ideal_max:.1f} kg to reach healthy range.\n\n"
        elif bmi >= 25:
            recommendations += f"Your BMI indicates you're overweight. Target: lose {current_weight - ideal_max:.1f} kg to reach healthy range.\n\n"
        else:
            recommendations += "Congratulations! You're in the healthy weight range. Focus on maintenance and overall fitness.\n\n"
        
        # Nutrition Plan
        recommendations += "🥗 Nutrition Recommendations\n"
        nutrition_tips = self.get_nutrition_tips(bmi, self.goal.get(), self.fitness_level.get())
        for tip in nutrition_tips:
            recommendations += f"• {tip}\n"
        recommendations += "\n"
        
        # Exercise Plan
        recommendations += "🏋️ Exercise Recommendations\n"
        exercise_tips = self.get_exercise_tips(bmi, self.goal.get(), self.fitness_level.get(), self.desired_body_type.get())
        for tip in exercise_tips:
            recommendations += f"• {tip}\n"
        recommendations += "\n"
        
        # Lifestyle Tips
        recommendations += "🌟 Lifestyle Tips\n"
        lifestyle_tips = self.get_lifestyle_tips(self.fitness_level.get())
        for tip in lifestyle_tips:
            recommendations += f"• {tip}\n"
        
        # Insert all at once
        self.recommendations_text.insert('1.0', recommendations)
        
        # Disable to prevent editing
        self.recommendations_text.config(state=tk.DISABLED)
    
    def get_nutrition_tips(self, bmi, goal, fitness_level):
        """Generate nutrition tips based on user profile"""
        tips = []
        
        # Base tips for everyone
        tips.append("Drink at least 8-10 glasses of water daily")
        tips.append("Eat 5-6 small meals throughout the day to boost metabolism")
        
        # BMI-specific tips
        if bmi < 18.5:
            tips.append("Increase caloric intake by 300-500 calories per day")
            tips.append("Focus on nutrient-dense foods: nuts, avocados, whole grains")
            tips.append("Add healthy fats: olive oil, nuts, fatty fish")
            tips.append("Protein: 1.6-2.2g per kg body weight (lean meats, eggs, dairy)")
        elif bmi >= 30:
            tips.append("Create a caloric deficit of 500-750 calories per day")
            tips.append("Eliminate sugary drinks and processed foods")
            tips.append("Fill half your plate with vegetables")
            tips.append("Lean protein: chicken breast, fish, legumes (1.2-1.6g/kg)")
            tips.append("Avoid late-night eating (stop 3 hours before bed)")
        elif bmi >= 25:
            tips.append("Moderate caloric deficit of 300-500 calories per day")
            tips.append("Reduce refined carbs, increase whole grains")
            tips.append("Protein: 1.4-1.8g per kg body weight")
            tips.append("Healthy snacks: Greek yogurt, fruits, nuts (portion-controlled)")
        else:
            tips.append("Maintain balanced macros: 40% carbs, 30% protein, 30% fats")
            tips.append("Protein: 1.2-1.6g per kg body weight")
            tips.append("Include variety: all food groups in moderation")
        
        # Goal-specific tips
        if goal == "gain muscle":
            tips.append("Increase protein to 1.8-2.2g per kg body weight")
            tips.append("Eat protein within 30 mins post-workout")
            tips.append("Complex carbs pre-workout: oats, brown rice, sweet potato")
        elif goal == "lose weight":
            tips.append("Track calories using an app (MyFitnessPal recommended)")
            tips.append("Increase fiber intake: vegetables, fruits, whole grains")
            tips.append("Limit sodium to reduce water retention")
        
        # Fitness level specific
        if fitness_level == "advanced":
            tips.append("Consider carb cycling: high carbs on training days")
            tips.append("Time your nutrients around workouts for optimal performance")
        
        return tips
    
    def get_exercise_tips(self, bmi, goal, fitness_level, desired_body):
        """Generate exercise tips based on user profile"""
        tips = []
        
        # Fitness level base recommendations
        if fitness_level == "beginner":
            tips.append("Start with 3-4 days per week, 30-45 minutes per session")
            tips.append("Walking/light jogging: 20-30 mins, 3x per week")
            tips.append("Bodyweight exercises: squats, push-ups, planks (2 sets of 10)")
            tips.append("Focus on proper form over intensity")
            tips.append("Rest days are crucial - take 1-2 days between workouts")
        elif fitness_level == "intermediate":
            tips.append("Train 4-5 days per week, 45-60 minutes per session")
            tips.append("Mix cardio and strength training")
            tips.append("Cardio: running, cycling, or swimming 3x per week")
            tips.append("Strength training: 3x per week (upper/lower split)")
        else:  # advanced
            tips.append("Train 5-6 days per week with varied intensity")
            tips.append("Implement progressive overload principles")
            tips.append("Advanced splits: push/pull/legs or upper/lower")
        
        # BMI-specific recommendations
        if bmi < 18.5:
            tips.append("Focus on strength training over cardio (70/30 split)")
            tips.append("Compound movements: deadlifts, squats, bench press")
            tips.append("Limit cardio to 2x per week, 20 mins max")
        elif bmi >= 30:
            tips.append("Low-impact cardio: swimming, cycling, elliptical")
            tips.append("Start with 15-20 mins, gradually increase to 45 mins")
            tips.append("Strength training 2x per week to preserve muscle")
            tips.append("Include flexibility work: yoga or stretching")
        elif bmi >= 25:
            tips.append("Cardio 4x per week: HIIT or steady-state (30-40 mins)")
            tips.append("Strength training 3x per week (full body or split)")
            tips.append("Include active recovery: walking, swimming")
        
        # Desired body type recommendations
        if desired_body == "muscular":
            tips.append("Heavy compound lifts: 4-6 reps, 4-5 sets")
            tips.append("Focus: deadlifts, squats, bench press, rows")
            tips.append("Progressive overload: increase weight weekly")
        elif desired_body == "lean":
            tips.append("Circuit training: high reps (12-15), short rest (30 secs)")
            tips.append("Mix cardio with resistance training")
            tips.append("HIIT sessions 2-3x per week")
        elif desired_body == "athletic":
            tips.append("Functional training: kettlebells, TRX, battle ropes")
            tips.append("Plyometrics: box jumps, burpees, jump squats")
            tips.append("Sport-specific training if applicable")
        
        # Goal-specific
        if goal == "lose weight":
            tips.append("Create caloric burn: aim for 300-500 calories per session")
            tips.append("Increase daily steps to 10,000+")
        elif goal == "gain muscle":
            tips.append("Limit cardio to preserve muscle mass")
            tips.append("Focus on progressive overload in strength training")
        
        return tips
    
    def get_lifestyle_tips(self, fitness_level):
        """Generate general lifestyle tips"""
        tips = [
            "Sleep 7-9 hours per night for optimal recovery",
            "Manage stress through meditation or deep breathing (10 mins daily)",
            "Track your progress weekly: weight, measurements, photos",
            "Be consistent - results take 8-12 weeks to show",
            "Find a workout buddy for accountability",
            "Prepare meals in advance to avoid unhealthy choices",
            "Listen to your body - rest when needed to prevent injury"
        ]
        
        if fitness_level == "beginner":
            tips.append("Start small and build sustainable habits")
            tips.append("Don't compare yourself to others - focus on your progress")
        elif fitness_level == "advanced":
            tips.append("Consider working with a coach for specialized programming")
            tips.append("Periodize your training to avoid plateaus")
        
        return tips


def main():
    root = tk.Tk()
    app = VexineApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
