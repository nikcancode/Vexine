import tkinter as tk
from tkinter import ttk, messagebox
import math


class VexineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("VEXINE - Advanced Health Guide")
        
        # FULLSCREEN
        self.root.attributes('-fullscreen', True)
        self.root.bind('<Escape>', lambda e: self.root.attributes('-fullscreen', False))
        self.root.bind('<F11>', lambda e: self.root.attributes('-fullscreen', 
                    not self.root.attributes('-fullscreen')))
        
        # Futuristic Dark Color Scheme
        self.colors = {
            'bg': '#0a0a0a',              # Pure black
            'bg_secondary': '#1a1a1a',    # Dark gray
            'primary': '#00ff9f',         # Neon green
            'secondary': '#00d4ff',       # Neon cyan
            'accent': '#ff0080',          # Neon pink
            'card': '#151515',            # Dark card
            'card_border': '#2a2a2a',     # Subtle border
            'text': '#ffffff',            # White text
            'text_dim': '#888888',        # Gray text
            'success': '#00ff9f',         # Green
            'warning': '#ffaa00',         # Orange
            'danger': '#ff0055',          # Red
            'glow': '#00ff9f'             # Glow effect
        }
        
        # Configure root
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
        self.activity_level = tk.StringVar(value="moderate")
        
        # Result variables
        self.bmi_value = 0
        self.maintenance_calories = 0
        self.surplus_calories = 0
        self.deficit_calories = 0
        
        # Page container
        self.current_page = None
        
        # Configure dropdown style
        self.configure_dropdown_style()
        
        # Show input page
        self.show_input_page()
    
    def configure_dropdown_style(self):
        """Configure custom dropdown style with blue text on black background"""
        style = ttk.Style()
        style.theme_use('default')
        
        # Configure the combobox
        style.configure('Custom.TCombobox',
                       fieldbackground='#000000',  # Black background
                       background='#000000',
                       foreground=self.colors['secondary'],  # Blue text
                       arrowcolor=self.colors['secondary'],
                       bordercolor=self.colors['secondary'],
                       lightcolor='#000000',
                       darkcolor='#000000',
                       selectbackground=self.colors['secondary'],
                       selectforeground='#000000')
        
        # Map for different states
        style.map('Custom.TCombobox',
                 fieldbackground=[('readonly', '#000000')],
                 foreground=[('readonly', self.colors['secondary'])],
                 selectbackground=[('readonly', self.colors['secondary'])],
                 selectforeground=[('readonly', '#000000')])
        
        # Configure the dropdown listbox
        self.root.option_add('*TCombobox*Listbox.background', '#000000')
        self.root.option_add('*TCombobox*Listbox.foreground', self.colors['secondary'])
        self.root.option_add('*TCombobox*Listbox.selectBackground', self.colors['secondary'])
        self.root.option_add('*TCombobox*Listbox.selectForeground', '#000000')
        self.root.option_add('*TCombobox*Listbox.font', ('Orbitron', 10, 'bold'))
    
    def clear_page(self):
        """Clear current page"""
        if self.current_page:
            self.current_page.destroy()
    
    def reset_inputs(self):
        """Reset all input fields to default values"""
        self.age.set(25)
        self.gender.set("male")
        self.height_cm.set(170.0)
        self.weight_kg.set(70.0)
        self.current_body_type.set("average")
        self.desired_body_type.set("athletic")
        self.fitness_level.set("beginner")
        self.goal.set("maintain")
        self.activity_level.set("moderate")
    
    def show_input_page(self):
        """Display the input page with full-width layout"""
        self.clear_page()
        
        self.current_page = tk.Frame(self.root, bg=self.colors['bg'])
        self.current_page.pack(fill=tk.BOTH, expand=True)
        
        # Header with only VEXINE
        header = tk.Frame(self.current_page, bg=self.colors['bg_secondary'], height=100)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        # Neon line
        tk.Frame(header, bg=self.colors['primary'], height=3).pack(fill=tk.X)
        
        # VEXINE title centered
        tk.Label(
            header,
            text="VEXINE",
            font=('Orbitron', 48, 'bold'),
            bg=self.colors['bg_secondary'],
            fg=self.colors['primary']
        ).pack(expand=True)
        
        # Subtitle below header
        subtitle_frame = tk.Frame(self.current_page, bg=self.colors['bg'])
        subtitle_frame.pack(pady=(20, 0))
        
        tk.Label(
            subtitle_frame,
            text="INITIALIZE HEALTH PROFILE",
            font=('Orbitron', 12),
            bg=self.colors['bg'],
            fg=self.colors['secondary']
        ).pack()
        
        # Main content container with padding
        content_container = tk.Frame(self.current_page, bg=self.colors['bg'])
        content_container.pack(fill=tk.BOTH, expand=True, padx=80, pady=30)
        
        # Grid layout - 3 columns across full width
        col1 = tk.Frame(content_container, bg=self.colors['bg'])
        col1.grid(row=0, column=0, padx=20, sticky='nsew')
        
        col2 = tk.Frame(content_container, bg=self.colors['bg'])
        col2.grid(row=0, column=1, padx=20, sticky='nsew')
        
        col3 = tk.Frame(content_container, bg=self.colors['bg'])
        col3.grid(row=0, column=2, padx=20, sticky='nsew')
        
        # Configure grid weights for equal distribution
        content_container.grid_columnconfigure(0, weight=1)
        content_container.grid_columnconfigure(1, weight=1)
        content_container.grid_columnconfigure(2, weight=1)
        
        # Column 1 - Biometric Data
        self.create_futuristic_card(col1, "BIOMETRIC DATA", [
            ("AGE", self.age, 10, 100, 1),
            ("HEIGHT", self.height_cm, 100, 250, 0.5, "CM"),
            ("WEIGHT", self.weight_kg, 30, 200, 0.5, "KG")
        ], color=self.colors['secondary'])
        
        gender_card = self.create_empty_card(col1, "GENDER PROFILE")
        self.create_neon_radio_group(gender_card, self.gender, 
                                     [("MALE", "male"), ("FEMALE", "female")])
        
        # Column 2 - Body Profile & Goals
        body_card = self.create_empty_card(col2, "BODY PROFILE")
        tk.Label(body_card, text="CURRENT", font=('Orbitron', 9, 'bold'),
                bg=self.colors['card'], fg=self.colors['secondary']).pack(pady=(10,5))
        self.create_neon_dropdown(body_card, self.current_body_type,
                                  ["underweight", "average", "athletic", "overweight", "obese"])
        
        tk.Label(body_card, text="TARGET", font=('Orbitron', 9, 'bold'),
                bg=self.colors['card'], fg=self.colors['secondary']).pack(pady=(20,5))
        self.create_neon_dropdown(body_card, self.desired_body_type,
                                  ["lean", "athletic", "muscular", "maintain"])
        
        goal_card = self.create_empty_card(col2, "PRIMARY GOAL")
        self.create_neon_dropdown(goal_card, self.goal,
                                  ["lose weight", "gain muscle", "maintain", "improve fitness"])
        
        # Column 3 - Fitness & Activity
        activity_card = self.create_empty_card(col3, "ACTIVITY LEVEL")
        self.create_neon_dropdown(activity_card, self.activity_level, 
                                  ["sedentary", "light", "moderate", "active", "very active"])
        
        fitness_card = self.create_empty_card(col3, "FITNESS LEVEL")
        self.create_neon_dropdown(fitness_card, self.fitness_level,
                                  ["beginner", "intermediate", "advanced"])
        
        # Calculate button at bottom spanning full width
        btn_frame = tk.Frame(content_container, bg=self.colors['bg'])
        btn_frame.grid(row=1, column=0, columnspan=3, pady=50)
        
        calc_btn = tk.Button(
            btn_frame,
            text="⚡ CALCULATE & ANALYZE ⚡",
            font=('Orbitron', 18, 'bold'),
            bg=self.colors['primary'],
            fg='#000000',
            activebackground=self.colors['secondary'],
            activeforeground='#000000',
            cursor='hand2',
            relief=tk.FLAT,
            padx=80,
            pady=25,
            command=self.calculate_and_proceed
        )
        calc_btn.pack()
        
        # Hover effect
        calc_btn.bind('<Enter>', lambda e: calc_btn.config(bg=self.colors['secondary']))
        calc_btn.bind('<Leave>', lambda e: calc_btn.config(bg=self.colors['primary']))
    
    def show_results_page(self):
        """Display the results page with compact layout"""
        self.clear_page()
        
        self.current_page = tk.Frame(self.root, bg=self.colors['bg'])
        self.current_page.pack(fill=tk.BOTH, expand=True)
        
        # Neon line at the very top
        tk.Frame(self.current_page, bg=self.colors['primary'], height=3).pack(fill=tk.X)
        
        # Header with back and recalculate buttons - REDUCED HEIGHT TO 125
        header_frame = tk.Frame(self.current_page, bg=self.colors['bg_secondary'], height=125)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        # Container for buttons and title
        header_content = tk.Frame(header_frame, bg=self.colors['bg_secondary'])
        header_content.pack(fill=tk.BOTH, expand=True)
        
        # Back button (left side)
        back_btn_header = tk.Button(
            header_content,
            text="← BACK",
            font=('Orbitron', 11, 'bold'),
            bg=self.colors['bg_secondary'],
            fg=self.colors['primary'],
            activebackground=self.colors['card'],
            activeforeground=self.colors['primary'],
            cursor='hand2',
            relief=tk.FLAT,
            padx=20,
            pady=10,
            command=self.show_input_page
        )
        back_btn_header.pack(side=tk.LEFT, padx=20, pady=12)
        
        back_btn_header.bind('<Enter>', lambda e: back_btn_header.config(bg=self.colors['card']))
        back_btn_header.bind('<Leave>', lambda e: back_btn_header.config(bg=self.colors['bg_secondary']))
        
        # Recalculate button (right side)
        recalc_btn_header = tk.Button(
            header_content,
            text="RECALCULATE →",
            font=('Orbitron', 11, 'bold'),
            bg=self.colors['bg_secondary'],
            fg=self.colors['primary'],
            activebackground=self.colors['card'],
            activeforeground=self.colors['primary'],
            cursor='hand2',
            relief=tk.FLAT,
            padx=20,
            pady=10,
            command=self.recalculate
        )
        recalc_btn_header.pack(side=tk.RIGHT, padx=20, pady=12)
        
        recalc_btn_header.bind('<Enter>', lambda e: recalc_btn_header.config(bg=self.colors['card']))
        recalc_btn_header.bind('<Leave>', lambda e: recalc_btn_header.config(bg=self.colors['bg_secondary']))
        
        # Title section (centered) - REDUCED FONT SIZES
        title_section = tk.Frame(header_content, bg=self.colors['bg_secondary'])
        title_section.place(relx=0.5, rely=0.5, anchor='center')
        
        tk.Label(
            title_section,
            text="ANALYSIS COMPLETE",
            font=('Orbitron', 28, 'bold'),
            bg=self.colors['bg_secondary'],
            fg=self.colors['primary']
        ).pack(pady=(5, 2))
        
        tk.Label(
            title_section,
            text="YOUR PERSONALIZED HEALTH MATRIX",
            font=('Orbitron', 10),
            bg=self.colors['bg_secondary'],
            fg=self.colors['secondary']
        ).pack(pady=(0, 5))
        
        # Main content - REDUCED PADDING
        content = tk.Frame(self.current_page, bg=self.colors['bg'])
        content.pack(fill=tk.BOTH, expand=True, padx=50, pady=20)
        
        # Top section - Smaller BMI + 3 calorie cards
        top_section = tk.Frame(content, bg=self.colors['bg'])
        top_section.pack(fill=tk.X, pady=(0, 20))
        
        # Large BMI Card (left) - REDUCED SIZE
        self.create_large_bmi_card(top_section).pack(side=tk.LEFT, padx=(0, 15))
        
        # Calorie cards container (right)
        calorie_container = tk.Frame(top_section, bg=self.colors['bg'])
        calorie_container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # 3 Calorie cards in a row - REDUCED SIZE
        self.create_compact_metric_card(calorie_container, "MAINTENANCE", 
                                       f"{int(self.maintenance_calories)}", 
                                       "CALORIES/DAY",
                                       self.colors['secondary']).pack(side=tk.LEFT, padx=8, fill=tk.BOTH, expand=True)
        
        self.create_compact_metric_card(calorie_container, "SURPLUS", 
                                       f"+{int(self.surplus_calories - self.maintenance_calories)}", 
                                       "BULK PHASE",
                                       self.colors['success']).pack(side=tk.LEFT, padx=8, fill=tk.BOTH, expand=True)
        
        self.create_compact_metric_card(calorie_container, "DEFICIT", 
                                       f"-{int(self.maintenance_calories - self.deficit_calories)}", 
                                       "CUT PHASE",
                                       self.colors['danger']).pack(side=tk.LEFT, padx=8, fill=tk.BOTH, expand=True)
        
        # Bottom section - 3 recommendation columns - MORE SPACE
        rec_section = tk.Frame(content, bg=self.colors['bg'])
        rec_section.pack(fill=tk.BOTH, expand=True)
        
        # Configure equal grid weights
        rec_section.grid_columnconfigure(0, weight=1)
        rec_section.grid_columnconfigure(1, weight=1)
        rec_section.grid_columnconfigure(2, weight=1)
        
        # Three columns for recommendations - USING GRID FOR EQUAL SIZING
        nutrition_col = tk.Frame(rec_section, bg=self.colors['bg'])
        nutrition_col.grid(row=0, column=0, sticky='nsew', padx=(0, 8))
        
        exercise_col = tk.Frame(rec_section, bg=self.colors['bg'])
        exercise_col.grid(row=0, column=1, sticky='nsew', padx=8)
        
        lifestyle_col = tk.Frame(rec_section, bg=self.colors['bg'])
        lifestyle_col.grid(row=0, column=2, sticky='nsew', padx=(8, 0))
        
        # Create recommendation sections
        self.create_recommendation_section(nutrition_col, "🥗 NUTRITION", 
                                          self.get_nutrition_tips(self.bmi_value, self.goal.get(), 
                                                                 self.fitness_level.get()))
        
        self.create_recommendation_section(exercise_col, "🏋️ TRAINING", 
                                          self.get_exercise_tips(self.bmi_value, self.goal.get(), 
                                                                self.fitness_level.get(), 
                                                                self.desired_body_type.get()))
        
        self.create_recommendation_section(lifestyle_col, "🌟 LIFESTYLE", 
                                          self.get_lifestyle_tips(self.fitness_level.get()))
    
    def recalculate(self):
        """Reset inputs and return to input page"""
        self.reset_inputs()
        self.show_input_page()
    
    def create_large_bmi_card(self, parent):
        """Create large BMI display card - REDUCED SIZE"""
        card = tk.Frame(parent, bg=self.colors['card'], width=280, height=200)
        card.pack_propagate(False)
        
        # Top colored line
        color = self.get_bmi_color(self.bmi_value)
        tk.Frame(card, bg=color, height=4).pack(fill=tk.X)
        
        tk.Label(
            card,
            text="BMI INDEX",
            font=('Orbitron', 11, 'bold'),
            bg=self.colors['card'],
            fg=self.colors['text_dim']
        ).pack(pady=(20, 5))
        
        tk.Label(
            card,
            text=f"{self.bmi_value:.1f}",
            font=('Orbitron', 56, 'bold'),
            bg=self.colors['card'],
            fg=color
        ).pack(pady=10)
        
        tk.Label(
            card,
            text=self.get_bmi_category(self.bmi_value),
            font=('Orbitron', 13, 'bold'),
            bg=self.colors['card'],
            fg=self.colors['text']
        ).pack()
        
        # BMI range indicator
        range_text = self.get_bmi_range_text(self.bmi_value)
        tk.Label(
            card,
            text=range_text,
            font=('Orbitron', 8),
            bg=self.colors['card'],
            fg=self.colors['text_dim']
        ).pack(pady=(5, 15))
        
        return card
    
    def create_compact_metric_card(self, parent, title, value, subtitle, color):
        """Create compact metric display card - REDUCED SIZE"""
        card = tk.Frame(parent, bg=self.colors['card'], height=110)
        card.pack_propagate(False)
        
        # Top colored line
        tk.Frame(card, bg=color, height=3).pack(fill=tk.X)
        
        tk.Label(
            card,
            text=title,
            font=('Orbitron', 8, 'bold'),
            bg=self.colors['card'],
            fg=self.colors['text_dim']
        ).pack(pady=(10, 3))
        
        tk.Label(
            card,
            text=value,
            font=('Orbitron', 22, 'bold'),
            bg=self.colors['card'],
            fg=color
        ).pack(pady=3)
        
        tk.Label(
            card,
            text=subtitle,
            font=('Orbitron', 7),
            bg=self.colors['card'],
            fg=self.colors['text_dim']
        ).pack(pady=(0, 8))
        
        return card
    
    def create_futuristic_card(self, parent, title, inputs, color=None):
        """Create futuristic input card"""
        if color is None:
            color = self.colors['primary']
            
        card = tk.Frame(parent, bg=self.colors['card'], relief=tk.FLAT, bd=0)
        card.pack(fill=tk.X, pady=15)
        
        # Title with neon border
        title_frame = tk.Frame(card, bg=color, height=3)
        title_frame.pack(fill=tk.X)
        
        tk.Label(
            card,
            text=title,
            font=('Orbitron', 12, 'bold'),
            bg=self.colors['card'],
            fg=color,
            pady=15
        ).pack()
        
        # Input fields
        for input_data in inputs:
            label_text = input_data[0]
            variable = input_data[1]
            from_ = input_data[2]
            to = input_data[3]
            increment = input_data[4]
            unit = input_data[5] if len(input_data) > 5 else ""
            
            input_frame = tk.Frame(card, bg=self.colors['card'])
            input_frame.pack(pady=8, padx=20)
            
            tk.Label(
                input_frame,
                text=label_text,
                font=('Orbitron', 9, 'bold'),
                bg=self.colors['card'],
                fg=self.colors['text_dim'],
                width=10
            ).pack(side=tk.LEFT, padx=5)
            
            spinbox = tk.Spinbox(
                input_frame,
                from_=from_,
                to=to,
                textvariable=variable,
                width=12,
                font=('Orbitron', 11, 'bold'),
                bg='#000000',
                fg=self.colors['secondary'],
                buttonbackground=self.colors['card_border'],
                relief=tk.FLAT,
                increment=increment,
                insertbackground=self.colors['primary']
            )
            spinbox.pack(side=tk.LEFT, padx=5)
            
            if unit:
                tk.Label(
                    input_frame,
                    text=unit,
                    font=('Orbitron', 9),
                    bg=self.colors['card'],
                    fg=self.colors['text_dim']
                ).pack(side=tk.LEFT, padx=5)
        
        tk.Frame(card, bg=self.colors['bg'], height=15).pack()
    
    def create_empty_card(self, parent, title):
        """Create empty card for custom content"""
        card = tk.Frame(parent, bg=self.colors['card'], relief=tk.FLAT, bd=0)
        card.pack(fill=tk.X, pady=15)
        
        title_frame = tk.Frame(card, bg=self.colors['secondary'], height=3)
        title_frame.pack(fill=tk.X)
        
        tk.Label(
            card,
            text=title,
            font=('Orbitron', 12, 'bold'),
            bg=self.colors['card'],
            fg=self.colors['secondary'],
            pady=15
        ).pack()
        
        return card
    
    def create_neon_radio_group(self, parent, variable, options):
        """Create neon radio button group"""
        frame = tk.Frame(parent, bg=self.colors['card'])
        frame.pack(pady=10)
        
        for text, value in options:
            rb = tk.Radiobutton(
                frame,
                text=text,
                variable=variable,
                value=value,
                font=('Orbitron', 10, 'bold'),
                bg=self.colors['card'],
                fg=self.colors['secondary'],
                activebackground=self.colors['card'],
                activeforeground=self.colors['secondary'],
                selectcolor=self.colors['bg_secondary'],
                cursor='hand2'
            )
            rb.pack(side=tk.LEFT, padx=15)
        
        tk.Frame(parent, bg=self.colors['bg'], height=15).pack()
    
    def create_neon_dropdown(self, parent, variable, values):
        """Create neon styled dropdown with blue text on black background"""
        combo = ttk.Combobox(
            parent,
            textvariable=variable,
            values=values,
            state='readonly',
            font=('Orbitron', 10, 'bold'),
            style='Custom.TCombobox',
            width=20
        )
        combo.pack(pady=10)
        
        tk.Frame(parent, bg=self.colors['bg'], height=15).pack()
    
    def create_recommendation_section(self, parent, title, tips):
        """Create scrollable recommendation section"""
        # Container
        container = tk.Frame(parent, bg=self.colors['card'])
        container.pack(fill=tk.BOTH, expand=True)
        
        # Title bar
        title_bar = tk.Frame(container, bg=self.colors['accent'], height=3)
        title_bar.pack(fill=tk.X)
        
        tk.Label(
            container,
            text=title,
            font=('Orbitron', 11, 'bold'),
            bg=self.colors['card'],
            fg=self.colors['accent'],
            pady=10
        ).pack()
        
        # Scrollable text frame
        text_frame = tk.Frame(container, bg=self.colors['card'])
        text_frame.pack(fill=tk.BOTH, expand=True, padx=12, pady=8)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(text_frame, bg=self.colors['card_border'])
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Text widget
        text_widget = tk.Text(
            text_frame,
            wrap=tk.WORD,
            font=('Consolas', 8),
            bg=self.colors['bg_secondary'],
            fg=self.colors['text'],
            yscrollcommand=scrollbar.set,
            relief=tk.FLAT,
            padx=8,
            pady=8,
            insertbackground=self.colors['primary']
        )
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Configure scrollbar
        scrollbar.config(command=text_widget.yview)
        
        # Insert tips
        for tip in tips:
            text_widget.insert(tk.END, f"▸ {tip}\n\n")
        
        text_widget.config(state=tk.DISABLED)
    
    def calculate_and_proceed(self):
        """Calculate BMI and calories, then show results"""
        try:
            # Get values
            height_m = self.height_cm.get() / 100
            weight = self.weight_kg.get()
            age = self.age.get()
            gender = self.gender.get()
            activity = self.activity_level.get()
            
            # Validate
            if height_m <= 0 or weight <= 0:
                messagebox.showerror("ERROR", "Invalid height or weight values!")
                return
            
            # Calculate BMI
            self.bmi_value = weight / (height_m ** 2)
            
            # Calculate calories using Mifflin-St Jeor Equation
            if gender == "male":
                bmr = (10 * weight) + (6.25 * self.height_cm.get()) - (5 * age) + 5
            else:
                bmr = (10 * weight) + (6.25 * self.height_cm.get()) - (5 * age) - 161
            
            # Activity multipliers
            activity_multipliers = {
                "sedentary": 1.2,
                "light": 1.375,
                "moderate": 1.55,
                "active": 1.725,
                "very active": 1.9
            }
            
            multiplier = activity_multipliers.get(activity, 1.55)
            self.maintenance_calories = bmr * multiplier
            self.surplus_calories = self.maintenance_calories + 300
            self.deficit_calories = self.maintenance_calories - 500
            
            # Show results page
            self.show_results_page()
            
        except Exception as e:
            messagebox.showerror("ERROR", f"Calculation failed: {str(e)}")
    
    def get_bmi_category(self, bmi):
        """Get BMI category"""
        if bmi < 18.5:
            return "UNDERWEIGHT"
        elif 18.5 <= bmi < 25:
            return "NORMAL"
        elif 25 <= bmi < 30:
            return "OVERWEIGHT"
        else:
            return "OBESE"
    
    def get_bmi_color(self, bmi):
        """Get color based on BMI"""
        if bmi < 18.5:
            return self.colors['secondary']
        elif 18.5 <= bmi < 25:
            return self.colors['success']
        elif 25 <= bmi < 30:
            return self.colors['warning']
        else:
            return self.colors['danger']
    
    def get_bmi_range_text(self, bmi):
        """Get BMI range information"""
        if bmi < 18.5:
            return "< 18.5 Range"
        elif 18.5 <= bmi < 25:
            return "18.5 - 24.9 Range"
        elif 25 <= bmi < 30:
            return "25.0 - 29.9 Range"
        else:
            return "≥ 30.0 Range"
    
    def get_nutrition_tips(self, bmi, goal, fitness_level):
        """Generate nutrition tips"""
        tips = []
        
        tips.append("Hydration: 3-4 liters of water daily minimum")
        tips.append("Meal frequency: 5-6 small meals for optimal metabolism")
        
        if bmi < 18.5:
            tips.append("Caloric surplus: +300-500 calories above maintenance")
            tips.append("Protein: 1.8-2.2g per kg bodyweight daily")
            tips.append("Healthy fats: Nuts, avocados, olive oil, fatty fish")
            tips.append("Dense carbs: Oats, rice, pasta, sweet potatoes")
        elif bmi >= 30:
            tips.append("Caloric deficit: -500-750 calories below maintenance")
            tips.append("Protein: 1.6-2.0g per kg to preserve muscle mass")
            tips.append("Eliminate: Sugary drinks, processed foods, refined carbs")
            tips.append("High volume: Fill 50% of plate with vegetables")
            tips.append("Meal timing: Stop eating 3 hours before bed")
        elif bmi >= 25:
            tips.append("Moderate deficit: -300-500 calories daily")
            tips.append("Protein: 1.4-1.8g per kg bodyweight")
            tips.append("Complex carbs: Switch to whole grains, reduce refined carbs")
            tips.append("Smart snacking: Greek yogurt, nuts (portioned), fruits")
        else:
            tips.append("Balanced macros: 40% carbs / 30% protein / 30% fats")
            tips.append("Protein: 1.2-1.6g per kg for maintenance")
            tips.append("Food variety: Include all food groups in moderation")
        
        if goal == "gain muscle":
            tips.append("Post-workout: 30g protein within 30 mins")
            tips.append("Pre-workout carbs: Oats, banana, rice for energy")
            tips.append("Protein boost: Increase to 2.0-2.2g per kg")
        elif goal == "lose weight":
            tips.append("Tracking: Use MyFitnessPal or similar app")
            tips.append("Fiber: 30g+ daily from vegetables and fruits")
            tips.append("Sodium: Limit to reduce water retention")
        
        if fitness_level == "advanced":
            tips.append("Nutrient timing: Carb cycling on training days")
            tips.append("Supplements: Consider creatine, protein powder, BCAAs")
        
        return tips
    
    def get_exercise_tips(self, bmi, goal, fitness_level, desired_body):
        """Generate exercise tips"""
        tips = []
        
        if fitness_level == "beginner":
            tips.append("Frequency: 3-4 sessions per week, 30-45 mins each")
            tips.append("Cardio foundation: Walking/jogging 20-30 mins, 3x weekly")
            tips.append("Bodyweight basics: Squats, push-ups, planks (2x10 reps)")
            tips.append("Form first: Master technique before adding weight")
            tips.append("Recovery: 48 hours rest between training same muscles")
        elif fitness_level == "intermediate":
            tips.append("Frequency: 4-5 sessions weekly, 45-60 mins each")
            tips.append("Split training: Upper/lower or push/pull/legs")
            tips.append("Cardio: 30-40 mins, 3x weekly (running, cycling, swimming)")
            tips.append("Progressive overload: Increase weight 2.5-5% weekly")
        else:
            tips.append("Frequency: 5-6 sessions weekly, varied intensity")
            tips.append("Advanced splits: PPL or bro-split with periodization")
            tips.append("Intensity techniques: Drop sets, supersets, rest-pause")
            tips.append("Deload week: Every 4-6 weeks reduce volume by 50%")
        
        if bmi < 18.5:
            tips.append("Strength focus: 70% resistance, 30% cardio")
            tips.append("Compounds: Deadlifts, squats, bench press, rows (4x6-8)")
            tips.append("Cardio limit: 2x weekly maximum, 20 mins sessions")
        elif bmi >= 30:
            tips.append("Low-impact cardio: Swimming, cycling, elliptical")
            tips.append("Duration: Start 15-20 mins, progress to 45 mins")
            tips.append("Resistance: 2x weekly to preserve muscle mass")
            tips.append("Flexibility: Daily stretching or yoga for mobility")
        elif bmi >= 25:
            tips.append("HIIT training: 20-30 mins, 3-4x weekly")
            tips.append("Resistance: 3x weekly full-body or split routine")
            tips.append("Active recovery: Walking, swimming on rest days")
        
        if desired_body == "muscular":
            tips.append("Heavy compounds: 4-6 reps, 4-5 sets, 80-85% 1RM")
            tips.append("Core lifts: Deadlift, squat, bench, OHP, rows")
            tips.append("Time under tension: Control eccentric phase (3 secs)")
        elif desired_body == "lean":
            tips.append("Circuit training: 12-15 reps, minimal rest (30s)")
            tips.append("Metabolic conditioning: Burpees, kettlebell swings")
            tips.append("HIIT: 30s work / 30s rest intervals, 20 mins")
        elif desired_body == "athletic":
            tips.append("Functional training: TRX, kettlebells, battle ropes")
            tips.append("Plyometrics: Box jumps, jump squats, burpees")
            tips.append("Agility: Ladder drills, cone drills, sprint intervals")
        
        if goal == "lose weight":
            tips.append("Calorie burn target: 300-500 per session")
            tips.append("Daily steps: Aim for 10,000+ via pedometer")
        elif goal == "gain muscle":
            tips.append("Cardio minimal: 2x weekly max to preserve mass")
            tips.append("Progressive overload: Track and beat lifts weekly")
        
        return tips
    
    def get_lifestyle_tips(self, fitness_level):
        """Generate lifestyle tips"""
        tips = [
            "Sleep priority: 7-9 hours nightly for recovery and hormones",
            "Stress management: 10 mins daily meditation or breathing",
            "Progress tracking: Weekly photos, measurements, weight log",
            "Consistency: Results visible after 8-12 weeks minimum",
            "Accountability: Training partner or coach recommended",
            "Meal prep: Prepare 3 days in advance to avoid bad choices",
            "Listen to body: Rest when fatigued to prevent injury",
            "Supplementation: Multivitamin, Vitamin D, Omega-3 basics"
        ]
        
        if fitness_level == "beginner":
            tips.append("Habit formation: Start small, build gradually")
            tips.append("No comparison: Focus on personal progress only")
            tips.append("Learning phase: Watch form videos, ask for help")
        elif fitness_level == "advanced":
            tips.append("Coaching: Consider hiring specialist for optimization")
            tips.append("Periodization: Plan mesocycles to avoid plateaus")
            tips.append("Recovery tools: Foam rolling, massage, ice baths")
            tips.append("Advanced metrics: Track HRV, sleep quality, readiness")
        
        return tips


def main():
    root = tk.Tk()
    app = VexineApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
