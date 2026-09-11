from django.db import migrations
from django.db.models import Max


NEW_TOP_CATEGORIES = [
    ('UPSC & Civil Services', 'civil'),
    ('Defence Exams', 'defence'),
    ('Teaching Exams', 'teaching'),
    ('State PSC', 'state'),
    ('Police & Constable', 'police'),
]

# parent category name -> [(sub-category name, logo_key), ...]
SUB_CATEGORIES = {
    'SSC': [
        ('SSC CGL', 'staff'),
        ('SSC CHSL', 'staff'),
        ('SSC GD Constable', 'staff'),
        ('SSC MTS', 'staff'),
    ],
    'Railway': [
        ('RRB NTPC', 'railway'),
        ('RRB Group D', 'railway'),
        ('RRB JE', 'railway'),
    ],
    'Banking & Insurance': [
        ('IBPS PO', 'banking'),
        ('IBPS Clerk', 'banking'),
        ('SBI PO', 'banking'),
        ('Insurance (LIC/NIACL)', 'insurance'),
    ],
    'NEET': [
        ('NEET Physics', 'science'),
        ('NEET Chemistry', 'science'),
        ('NEET Biology', 'science'),
    ],
    'JEE': [
        ('JEE Physics', 'science'),
        ('JEE Chemistry', 'science'),
        ('JEE Mathematics', 'maths'),
    ],
    'UPSC & Civil Services': [
        ('UPSC General Studies', 'civil'),
        ('UPSC CSAT', 'civil'),
    ],
    'Defence Exams': [
        ('NDA & NA', 'defence'),
        ('CDS', 'defence'),
    ],
    'Teaching Exams': [
        ('CTET Paper 1', 'teaching'),
        ('CTET Paper 2', 'teaching'),
    ],
    'State PSC': [
        ('UPPSC', 'state'),
        ('BPSC', 'state'),
    ],
    'Police & Constable': [
        ('UP Police Constable', 'police'),
        ('Sub-Inspector (SI)', 'police'),
    ],
}

TEST_SERIES_DATA = [
    {
        'name': 'SSC CGL Tier 1 Mock Test 1',
        'categories': ['SSC CGL'],
        'test_type': 'mock_test',
        'original_price': '499.00', 'current_price': '199.00',
        'duration_minutes': 60,
        'about': 'A full-length SSC CGL Tier 1 mock test covering reasoning, quantitative aptitude, English and general awareness.',
        'sections': [
            ('reasoning', 'General Intelligence & Reasoning', '0.25'),
            ('quant', 'Quantitative Aptitude', '0.25'),
            ('english', 'English Language', '0.25'),
            ('awareness', 'General Awareness', '0.25'),
        ],
        'questions': [
            ('reasoning', 'Choose the odd one out.', 'Cat', 'Dog', 'Cow', 'Sparrow', 'D'),
            ('reasoning', 'Find the next number in the series: 2, 6, 12, 20, __.', '24', '28', '30', '32', 'C'),
            ('quant', 'What is 25% of 480?', '100', '110', '120', '125', 'C'),
            ('quant', 'Two numbers are in the ratio 3:5 and their sum is 64. What is the smaller number?', '18', '24', '30', '40', 'B'),
            ('english', 'Choose the synonym of "Brief".', 'Lengthy', 'Short', 'Difficult', 'Late', 'B'),
            ('english', 'Choose the correctly spelled word.', 'Accomodation', 'Acommodation', 'Accommodation', 'Accommadation', 'C'),
            ('awareness', 'On which date was the Constitution of India adopted?', '15 August 1947', '26 January 1950', '26 November 1949', '2 October 1948', 'C'),
            ('awareness', 'Which is the largest planet in the Solar System?', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'C'),
        ],
    },
    {
        'name': 'RRB NTPC Practice Test 1',
        'categories': ['RRB NTPC'],
        'test_type': 'practice_test',
        'original_price': '399.00', 'current_price': '149.00',
        'duration_minutes': 60,
        'about': 'Railway RRB NTPC practice set with mathematics, reasoning and general awareness questions.',
        'sections': [
            ('maths', 'Mathematics', '0.33'),
            ('reasoning', 'General Intelligence & Reasoning', '0.33'),
            ('awareness', 'General Awareness', '0.33'),
        ],
        'questions': [
            ('maths', 'Convert 72 km/h into metres per second.', '18 m/s', '20 m/s', '22 m/s', '24 m/s', 'B'),
            ('maths', 'What is the LCM of 12 and 18?', '24', '30', '36', '48', 'C'),
            ('maths', 'If 15 workers complete a job in 12 days, how many days will 20 workers take at the same rate?', '8', '9', '10', '16', 'B'),
            ('reasoning', 'Find the next number: 3, 8, 15, 24, 35, __.', '44', '46', '48', '50', 'C'),
            ('reasoning', 'A is the brother of B, and B is the sister of C. How is A related to C?', 'Brother', 'Sister', 'Father', 'Cousin', 'A'),
            ('awareness', "India's first passenger train ran between which two places?", 'Delhi and Agra', 'Mumbai and Thane', 'Kolkata and Howrah', 'Chennai and Arakkonam', 'B'),
            ('awareness', 'What is the SI unit of force?', 'Joule', 'Pascal', 'Newton', 'Watt', 'C'),
            ('awareness', 'Deficiency of vitamin C causes which disease?', 'Rickets', 'Scurvy', 'Beriberi', 'Night blindness', 'B'),
        ],
    },
    {
        'name': 'IBPS PO Prelims Mock Test 1',
        'categories': ['IBPS PO'],
        'test_type': 'mock_test',
        'original_price': '499.00', 'current_price': '199.00',
        'duration_minutes': 60,
        'about': 'IBPS PO prelims style mock test with reasoning ability, quantitative aptitude and English language sections.',
        'sections': [
            ('reasoning', 'Reasoning Ability', '0.25'),
            ('quant', 'Quantitative Aptitude', '0.25'),
            ('english', 'English Language', '0.25'),
        ],
        'questions': [
            ('reasoning', 'Find the next number: 5, 11, 23, 47, __.', '71', '89', '95', '97', 'C'),
            ('reasoning', 'In a row of 30 people, Riya is 12th from the left. What is her position from the right?', '18th', '19th', '20th', '21st', 'B'),
            ('reasoning', 'If BANK is coded by moving every letter one step forward, what is the code?', 'CBOL', 'CAML', 'AZMJ', 'DBPM', 'A'),
            ('quant', 'What is 18% of 500?', '80', '85', '90', '95', 'C'),
            ('quant', 'Find the average of 18, 22, 25 and 15.', '18', '19', '20', '21', 'C'),
            ('quant', 'What is the compound interest on Rs. 1,000 at 10% per annum for 2 years?', 'Rs. 200', 'Rs. 210', 'Rs. 220', 'Rs. 240', 'B'),
            ('english', 'Choose the synonym of "Prudent".', 'Careless', 'Cautious', 'Noisy', 'Generous', 'B'),
            ('english', 'Choose the antonym of "Scarce".', 'Rare', 'Limited', 'Abundant', 'Small', 'C'),
        ],
    },
    {
        'name': 'NEET Full Mock Test 1',
        'categories': ['NEET Physics', 'NEET Chemistry', 'NEET Biology'],
        'test_type': 'mock_test',
        'original_price': '699.00', 'current_price': '299.00',
        'duration_minutes': 180,
        'marks': 4,
        'about': 'A full-length NEET mock test covering Physics, Chemistry and Biology in the real exam pattern.',
        'sections': [
            ('physics', 'Physics', '1.00'),
            ('chemistry', 'Chemistry', '1.00'),
            ('biology', 'Biology', '1.00'),
        ],
        'questions': [
            ('physics', 'What is the SI unit of electric field?', 'N/C', 'C/N', 'J·s', 'W/m', 'A'),
            ('physics', 'The slope of a velocity-time graph represents which quantity?', 'Displacement', 'Acceleration', 'Momentum', 'Force', 'B'),
            ('physics', 'Which lens is used to correct myopia?', 'Convex lens', 'Concave lens', 'Cylindrical lens', 'Bifocal lens only', 'B'),
            ('physics', 'What is the SI unit of power?', 'Joule', 'Newton', 'Watt', 'Pascal', 'C'),
            ('chemistry', 'What is the atomic number of oxygen?', '6', '7', '8', '16', 'C'),
            ('chemistry', 'The pH of gastric acid is closest to which value?', '2', '7', '9', '12', 'A'),
            ('chemistry', "What is the approximate value of Avogadro's constant?", '6.022 × 10²³', '3.0 × 10⁸', '9.8 × 10²', '1.6 × 10⁻¹⁹', 'A'),
            ('chemistry', 'Which gas is produced when zinc reacts with dilute hydrochloric acid?', 'Oxygen', 'Hydrogen', 'Carbon dioxide', 'Nitrogen', 'B'),
            ('biology', 'Which cell structure is the main site of protein synthesis?', 'Lysosome', 'Ribosome', 'Golgi apparatus', 'Centriole', 'B'),
            ('biology', 'What is the functional unit of the kidney?', 'Neuron', 'Alveolus', 'Nephron', 'Villus', 'C'),
            ('biology', 'Which hormone lowers blood glucose level?', 'Glucagon', 'Adrenaline', 'Insulin', 'Thyroxine', 'C'),
            ('biology', 'Who proposed the double-helix model of DNA?', 'Darwin and Wallace', 'Watson and Crick', 'Mendel and Morgan', 'Meselson and Stahl', 'B'),
        ],
    },
    {
        'name': 'JEE Main Full Mock Test 1',
        'categories': ['JEE Physics', 'JEE Chemistry', 'JEE Mathematics'],
        'test_type': 'mock_test',
        'original_price': '699.00', 'current_price': '299.00',
        'duration_minutes': 180,
        'marks': 4,
        'about': 'A full-length JEE Main mock test covering Physics, Chemistry and Mathematics in the real exam pattern.',
        'sections': [
            ('physics', 'Physics', '1.00'),
            ('chemistry', 'Chemistry', '1.00'),
            ('maths', 'Mathematics', '1.00'),
        ],
        'questions': [
            ('physics', 'What is the SI unit of force?', 'Joule', 'Newton', 'Pascal', 'Watt', 'B'),
            ('physics', 'Ignoring air resistance, the acceleration of a projectile is directed how?', 'Horizontally forward', 'Vertically upward', 'Vertically downward', 'Along its velocity', 'C'),
            ('physics', "Which expression gives the kinetic energy of a body of mass m moving with speed v?", 'mv', 'mv squared', 'one-half mv squared', '2mv squared', 'C'),
            ('physics', "Which equation represents Ohm's law?", 'V = IR', 'P = VI', 'F = ma', 'Q = It squared', 'A'),
            ('chemistry', 'What is the atomic number of carbon?', '4', '6', '8', '12', 'B'),
            ('chemistry', 'Which of the following is a noble gas?', 'Nitrogen', 'Oxygen', 'Argon', 'Chlorine', 'C'),
            ('chemistry', 'What is the hybridization of carbon in methane (CH4)?', 'sp', 'sp2', 'sp3', 'sp3d', 'C'),
            ('chemistry', 'Which is the most electronegative element?', 'Oxygen', 'Nitrogen', 'Chlorine', 'Fluorine', 'D'),
            ('maths', 'What is the derivative of sin(x)?', 'cos(x)', '-cos(x)', '-sin(x)', 'tan(x)', 'A'),
            ('maths', 'How many real roots does x² + 4 = 0 have?', '0', '1', '2', '4', 'A'),
            ('maths', 'What is the value of log₁₀(100)?', '1', '2', '10', '100', 'B'),
            ('maths', 'If A and B are independent events, P(A∩B) equals what?', 'P(A) + P(B)', 'P(A) − P(B)', 'P(A) × P(B)', 'P(A) / P(B)', 'C'),
        ],
    },
    {
        'name': 'UPSC Prelims GS Mock Test 1',
        'categories': ['UPSC General Studies'],
        'test_type': 'mock_test',
        'original_price': '599.00', 'current_price': '299.00',
        'duration_minutes': 120,
        'about': 'A balanced UPSC prelims practice test covering polity, history, geography and economy.',
        'sections': [
            ('polity', 'Indian Polity & Governance', '0.33'),
            ('general', 'History, Geography & Economy', '0.33'),
        ],
        'questions': [
            ('polity', 'On which date was the Constitution of India adopted?', '15 August 1947', '26 January 1950', '26 November 1949', '2 October 1948', 'C'),
            ('polity', 'Which amendment added Fundamental Duties to the Constitution of India?', '24th Amendment', '42nd Amendment', '44th Amendment', '73rd Amendment', 'B'),
            ('polity', 'Which article is associated with the Right to Constitutional Remedies?', 'Article 14', 'Article 19', 'Article 21', 'Article 32', 'D'),
            ('polity', 'The Goods and Services Tax was enabled by which Constitutional Amendment?', '91st', '97th', '101st', '103rd', 'C'),
            ('general', 'In which year did the Reserve Bank of India begin operations?', '1935', '1947', '1950', '1955', 'A'),
            ('general', 'Which Harappan site is well known for its ancient dockyard?', 'Kalibangan', 'Lothal', 'Rakhigarhi', 'Banawali', 'B'),
            ('general', 'Which is the largest Indian state by area?', 'Madhya Pradesh', 'Maharashtra', 'Rajasthan', 'Uttar Pradesh', 'C'),
            ('general', 'Which mountain range is older than the Himalayas?', 'Aravalli Range', 'Karakoram Range', 'Pir Panjal Range', 'Zanskar Range', 'A'),
        ],
    },
    {
        'name': 'NDA & CDS General Ability Test 1',
        'categories': ['NDA & NA', 'CDS'],
        'test_type': 'mock_test',
        'original_price': '499.00', 'current_price': '249.00',
        'duration_minutes': 120,
        'about': 'Defence entrance practice test covering general knowledge and elementary mathematics.',
        'sections': [
            ('gk', 'General Knowledge', '0.33'),
            ('maths', 'Elementary Mathematics', '0.33'),
        ],
        'questions': [
            ('gk', 'Which body conducts the National Defence Academy examination?', 'Staff Selection Commission', 'Union Public Service Commission', 'National Testing Agency', 'Indian Army', 'B'),
            ('gk', 'Where is the Officers Training Academy located?', 'Chennai', 'Pune', 'Dehradun', 'Kochi', 'A'),
            ('gk', "What is India's highest wartime gallantry award?", 'Ashoka Chakra', 'Maha Vir Chakra', 'Param Vir Chakra', 'Vir Chakra', 'C'),
            ('gk', 'Indian Army Day is observed on which date?', '15 January', '26 January', '4 December', '8 October', 'A'),
            ('maths', 'A vehicle travels at 60 km/h for 2 hours. What distance does it cover?', '30 km', '60 km', '90 km', '120 km', 'D'),
            ('maths', 'Find the next number: 2, 5, 10, 17, 26, __.', '33', '35', '37', '39', 'C'),
            ('maths', 'If 3x + 5 = 20, what is x?', '3', '4', '5', '6', 'C'),
            ('maths', 'What is the HCF of 24 and 36?', '6', '8', '12', '18', 'C'),
        ],
    },
    {
        'name': 'CTET Paper 1 Practice Test 1',
        'categories': ['CTET Paper 1'],
        'test_type': 'practice_test',
        'original_price': '299.00', 'current_price': '149.00',
        'duration_minutes': 90,
        'about': 'Practice child development, pedagogy, language, mathematics and environmental studies for CTET Paper I.',
        'sections': [
            ('pedagogy', 'Child Development & Pedagogy', '0.00'),
            ('subject', 'Language, Maths & EVS', '0.00'),
        ],
        'questions': [
            ('pedagogy', 'In child-centred education, the learner is primarily viewed as what?', 'A passive listener', 'An active participant', 'A silent observer', 'A note-copying assistant', 'B'),
            ('pedagogy', 'Formative assessment is generally conducted at what stage?', 'Only after the final examination', 'During the teaching-learning process', 'Before admission only', 'Only once each year', 'B'),
            ('pedagogy', 'Inclusive education aims to teach children with diverse needs in which setting?', 'Separate schools only', 'The same classroom with suitable support', 'Home study only', 'No structured setting', 'B'),
            ('pedagogy', 'The Zone of Proximal Development is associated with which psychologist?', 'Jean Piaget', 'B. F. Skinner', 'Lev Vygotsky', 'Sigmund Freud', 'C'),
            ('subject', 'What is three-fourths of 200?', '100', '125', '150', '175', 'C'),
            ('subject', 'What is the HCF of 24 and 36?', '6', '8', '12', '18', 'C'),
            ('subject', 'Choose the synonym of "rapid".', 'Slow', 'Swift', 'Quiet', 'Late', 'B'),
            ('subject', 'Which process changes liquid water into water vapour?', 'Condensation', 'Freezing', 'Evaporation', 'Precipitation', 'C'),
        ],
    },
    {
        'name': 'UPPSC Prelims Mock Test 1',
        'categories': ['UPPSC'],
        'test_type': 'mock_test',
        'original_price': '499.00', 'current_price': '249.00',
        'duration_minutes': 120,
        'about': 'A state civil services mock test covering Uttar Pradesh knowledge, polity and aptitude.',
        'sections': [
            ('state', 'Uttar Pradesh General Knowledge', '0.33'),
            ('aptitude', 'Polity & Aptitude', '0.33'),
        ],
        'questions': [
            ('state', 'What is the capital of Uttar Pradesh?', 'Kanpur', 'Lucknow', 'Agra', 'Varanasi', 'B'),
            ('state', 'The principal seat of the Allahabad High Court is in which city?', 'Lucknow', 'Noida', 'Prayagraj', 'Meerut', 'C'),
            ('state', 'Dudhwa National Park is located in which district?', 'Lakhimpur Kheri', 'Jhansi', 'Gorakhpur', 'Mathura', 'A'),
            ('state', 'The confluence of the Ganga, Yamuna and the mythical Saraswati is at which city?', 'Ayodhya', 'Prayagraj', 'Varanasi', 'Mirzapur', 'B'),
            ('aptitude', 'Who appoints the Governor of an Indian state?', 'Prime Minister', 'Chief Minister', 'President of India', 'Chief Justice of India', 'C'),
            ('aptitude', 'Which amendment gave constitutional status to Panchayati Raj institutions?', '42nd', '44th', '73rd', '86th', 'C'),
            ('aptitude', 'What is 15% of 640?', '86', '90', '96', '102', 'C'),
            ('aptitude', 'Find the next number: 4, 9, 16, 25, __.', '30', '32', '36', '49', 'C'),
        ],
    },
    {
        'name': 'UP Police Constable Mock Test 1',
        'categories': ['UP Police Constable'],
        'test_type': 'practice_test',
        'original_price': '199.00', 'current_price': '99.00',
        'duration_minutes': 90,
        'about': 'A practical police recruitment set with general awareness, reasoning, mathematics and language.',
        'sections': [
            ('awareness', 'General Awareness', '0.25'),
            ('aptitude', 'Reasoning & Aptitude', '0.25'),
        ],
        'questions': [
            ('awareness', 'What does FIR stand for?', 'First Investigation Record', 'First Information Report', 'Formal Incident Review', 'Federal Inquiry Report', 'B'),
            ('awareness', "What is India's single emergency response support number?", '100', '101', '108', '112', 'D'),
            ('awareness', 'A red traffic signal instructs a driver to do what?', 'Proceed slowly', 'Turn only', 'Stop', 'Sound the horn', 'C'),
            ('awareness', 'Article 21 of the Constitution protects which right?', 'Right to property', 'Life and personal liberty', 'Freedom of religion only', 'Right to vote', 'B'),
            ('aptitude', 'Two numbers are in the ratio 2:3 and total 50. What is the smaller number?', '10', '20', '25', '30', 'B'),
            ('aptitude', 'What is 20% of 450?', '45', '80', '90', '100', 'C'),
            ('aptitude', 'Choose the antonym of "lawful".', 'Legal', 'Valid', 'Unlawful', 'Formal', 'C'),
            ('aptitude', 'If all roses are flowers and some flowers fade quickly, which statement must be true?', 'All flowers are roses', 'All roses are flowers', 'No roses fade', 'No flowers are roses', 'B'),
        ],
    },
]


def seed_categories_and_test_series(apps, schema_editor):
    Category = apps.get_model('myapp', 'Category')
    Course = apps.get_model('myapp', 'Course')
    Question = apps.get_model('myapp', 'Question')
    TestSection = apps.get_model('myapp', 'TestSection')

    top_order = (Category.objects.filter(parent__isnull=True).aggregate(value=Max('order'))['value'] or 0) + 1
    for offset, (name, logo_key) in enumerate(NEW_TOP_CATEGORIES):
        category, created = Category.objects.get_or_create(
            name=name,
            defaults={'logo_key': logo_key, 'order': top_order + offset},
        )
        if not created and category.logo_key == 'general':
            category.logo_key = logo_key
            category.save(update_fields=['logo_key'])

    for parent_name, subs in SUB_CATEGORIES.items():
        parent = Category.objects.filter(name=parent_name, parent__isnull=True).first()
        if not parent:
            continue
        sub_order = (Category.objects.filter(parent=parent).aggregate(value=Max('order'))['value'] or 0) + 1
        for offset, (sub_name, logo_key) in enumerate(subs):
            sub_category, created = Category.objects.get_or_create(
                name=sub_name,
                defaults={'logo_key': logo_key, 'parent': parent, 'order': sub_order + offset},
            )
            if not created and sub_category.parent_id != parent.id:
                sub_category.parent = parent
                sub_category.save(update_fields=['parent'])

    course_order = (
        Course.objects.filter(course_type='test_series').aggregate(value=Max('order'))['value'] or 0
    ) + 1

    for course_offset, content in enumerate(TEST_SERIES_DATA):
        course, _ = Course.objects.get_or_create(
            course_type='test_series',
            name=content['name'],
            defaults={
                'test_type': content['test_type'],
                'original_price': content['original_price'],
                'current_price': content['current_price'],
                'duration_minutes': content['duration_minutes'],
                'max_optional_sections': 0,
                'about': content['about'],
                'order': course_order + course_offset,
                'is_active': True,
            },
        )

        leaf_categories = Category.objects.filter(name__in=content['categories'])
        course.categories.set(leaf_categories)

        sections = {}
        for section_order, (key, section_name, negative_marks) in enumerate(content['sections']):
            section, _ = TestSection.objects.get_or_create(
                course=course,
                name=section_name,
                defaults={
                    'is_optional': False,
                    'negative_marks': negative_marks,
                    'order': section_order,
                },
            )
            sections[key] = section

        for question_order, question_data in enumerate(content['questions']):
            section_key, text, option_a, option_b, option_c, option_d, correct_answer = question_data
            Question.objects.get_or_create(
                course=course,
                text=text,
                defaults={
                    'section': sections[section_key],
                    'question_type': 'single',
                    'option_a': option_a,
                    'option_b': option_b,
                    'option_c': option_c,
                    'option_d': option_d,
                    'correct_answer': correct_answer,
                    'marks': content.get('marks', 1),
                    'order': question_order,
                },
            )


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0079_alter_bannerslide_image_and_more'),
    ]

    operations = [
        migrations.RunPython(seed_categories_and_test_series, migrations.RunPython.noop),
    ]
