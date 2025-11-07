show databases;
create database ai_model_train;
use ai_model_train;

create table Researcher(
	ID int primary key auto_increment,
    Name varchar(50) not null,
    Email varchar(50) not null unique,
    Organization varchar(50),
    Role varchar(50) not null
);

create table Model(
	ID int primary key auto_increment,
    Name varchar(50) not null,
    Type varchar(50) not null,
    Framework varchar(50) not null,
    Researcher_ID int not null,
    Description text,
    foreign key (Researcher_ID) references Researcher(ID)
);

create table Model_Version(
	ID int primary key auto_increment,
    Model_ID int not null,
    Version varchar(50),
    Changes text not null,
    Date_Created date not null,
    foreign key (Model_ID) references Model(ID)
);

create table Dataset(
	ID int primary key auto_increment,
    Name varchar(50) not null,
    Source varchar(255) not null,
    Type varchar(50) not null,
    Size_GB float not null check(Size_GB > 0),
    Upload_Date date,
    License varchar(255) not null
);

create table Training(
	ID int primary key auto_increment,
    Model_ID int not null,
    Dataset_ID int not null,
    Date_Trained datetime,
    Epochs int,
    Batch_Size int,
	Learning_Rate float not null,
    Optimizer varchar(50),
    Status enum('pending','completed','failed') not null default 'pending',
    foreign key (Model_ID) references Model(ID),
    foreign key (Dataset_ID) references Dataset(ID)
);

create table Parameter(
	ID int primary key auto_increment,
    Training_ID int not null,
    Name varchar(50) not null,
    Value varchar(50) not null,
    foreign key (Training_ID) references Training(ID)
);

create table Performance(
	ID int primary key auto_increment,
    Training_ID int not null,
    Accuracy float not null,
    Model_Precision float not null,
    Recall float not null,
    F1_Score float not null,
    Loss float not null,
    Training_Time time not null,
    foreign key (Training_ID) references Training(ID)
);

create table Hardware_Config(
	ID int primary key auto_increment,
    Training_ID int not null,
    GPU_Type varchar(50),
    CPU_Type varchar(50),
    Ram varchar(50),
    foreign key (Training_ID) references Training(ID)
);

-- This trigger will add the updates date of a dataset automatically
DELIMITER $$
create trigger upload_date
before insert on Dataset
for each row
begin
	set new.Upload_Date = curdate();
end$$
DELIMITER ;

-- This trigger will update the status of a training model to pending and add the timestamp aswell
DELIMITER $$
create trigger training_start
before insert on Training
for each row
begin
	set new.Date_Trained = NOW();
    set new.Status = 'pending';
end$$
DELIMITER ;

-- This trigger will update the status and timestamp to complete when the performance of the model is added
DELIMITER $$
create trigger training_end
after insert on Performance
for each row
begin
    update Training
    set Status = 'completed'
    where ID = new.Training_ID;
end$$
DELIMITER ;

-- This trigger is going to update the stauts of a training to failed if certain requirements are not met
DELIMITER $$
create trigger training_fail
after insert on Performance
for each row
begin
    if new.Accuracy < 0.40 or new.Loss > 0.60 then
        UPDATE Training
        set Status = 'failed'
        where ID = new.Training_ID;
    end if;
end$$
DELIMITER ;

-- This view will display the resrachers with thier model data
create view view_researcher_models as
select 
    Researcher.ID as Researcher_ID,
    Researcher.Name as Researcher_Name,
    Researcher.Organization,
    Researcher.Role,
    Model.ID as Model_ID,
    Model.Name AS Model_Name,
    Model.Framework,
    Model.Type
from Researcher
join Model on Researcher.ID = Model.Researcher_ID;
SELECT * FROM view_researcher_models;

-- View hardware usage for each model
create view view_hardware_usage as
select 
    Hardware_Config.ID as Hardware_ID,
    Model.Name as Model_Name,
    Hardware_Config.GPU_Type,
    Hardware_Config.CPU_Type,
    Hardware_Config.Ram
from Hardware_Config
join Training on Hardware_Config.Training_ID = Training.ID
join Model on Training.Model_ID = Model.ID;
SELECT * FROM view_hardware_usage;

-- View training performance for each model
create view view_training_performance as
select 
    Performance.ID as Performance_ID,
    Model.Name as Model_Name,
    Performance.Accuracy,
    Performance.Model_Precision,
    Performance.Recall,
    Performance.F1_Score,
    Performance.Loss,
    Performance.Training_Time
from Performance
join Training on Performance.Training_ID = Training.ID
join Model on Training.Model_ID = Model.ID;
SELECT * FROM view_training_performance;

-- View failed Trainings
create view view_failed_trainings as
select
    Training.ID as Training_ID,
    Researcher.Name as Researcher_Name,
    Model.Name as Model_Name,
    Dataset.Name as Dataset_Name,
    Performance.Accuracy,
    Performance.Loss,
    Training.Status
from Training
join Model on Training.Model_ID = Model.ID
join Researcher on Model.Researcher_ID = Researcher.ID
join Dataset on Training.Dataset_ID = Dataset.ID
join Performance on Training.ID = Performance.Training_ID
where Training.Status = 'failed';
SELECT * FROM view_failed_trainings;

-- This is a store procedure that can show all the tranings done by the reascher name 
DELIMITER $$
create procedure GetTrainingsByResearcherName(in researcherName varchar(50))
begin
    select 
        Researcher.Name as Researcher_Name,
        Model.Name as Model_Name,
        Dataset.Name as Dataset_Name,
        Training.Status,
        Performance.Accuracy,
        Performance.Loss
    from Training
    join Model on Training.Model_ID = Model.ID
    join Researcher on Model.Researcher_ID = Researcher.ID
    join Dataset on Training.Dataset_ID = Dataset.ID
    join Performance on Training.ID = Performance.Training_ID
    where Researcher.Name = researcherName;
end$$
DELIMITER ;
call GetTrainingsByResearcherName('Ali Maqsood');

-- This store procedure will show us the average accuracy of a model
DELIMITER $$
create procedure GetModelAverageAccuracy(in modelName varchar(50))
begin
    select 
        Model.Name as Model_Name,
        round(avg(Performance.Accuracy),2) as Average_Accuracy
    from Model
    join Training on Model.ID = Training.Model_ID
    join Performance on Training.ID = Performance.Training_ID
    where Model.Name = modelName
    group by Model.Name;
end$$
DELIMITER ;
CALL GetModelAverageAccuracy('VisionNet');


-- ===========================
-- 🌟 TEST DATA FOR AI TRAINING DATABASE
-- ===========================
-- Researcher
INSERT INTO Researcher (Name, Email, Organization, Role) VALUES
('Dr. Sarah Khan', 'sarah.khan@aihub.org', 'AI Research Hub', 'Lead Scientist'),
('Ali Maqsood', 'ali.maqsood@superior.edu.pk', 'Superior University', 'AI Student'),
('Dr. John Lee', 'john.lee@mlvision.io', 'ML Vision Labs', 'Senior Researcher'),
('Dr. Ayesha Malik', 'ayesha.malik@deeplearn.pk', 'DeepLearn Pakistan', 'AI Engineer'),
('Michael Chen', 'michael.chen@autovision.ai', 'AutoVision AI', 'Research Engineer'),
('Fatima Zahra', 'fatima.zahra@datasense.org', 'DataSense Org', 'ML Specialist'),
('Omar Farooq', 'omar.farooq@nextgenml.io', 'NextGen ML', 'AI Researcher'),
('Dr. Lisa Wong', 'lisa.wong@genai.tech', 'GenAI Tech', 'Project Lead'),
('Noor Ahmed', 'noor.ahmed@superior.edu.pk', 'Superior University', 'Student Researcher'),
('David Kim', 'david.kim@robotics.ai', 'Robotics AI Lab', 'AI Architect');

-- 🧠 Model (10)
INSERT INTO Model (Name, Type, Framework, Researcher_ID, Description) VALUES
('VisionNet', 'Image Classification', 'TensorFlow', 1, 'CNN model for object recognition using ImageNet dataset.'),
('ChatBrain', 'NLP Transformer', 'PyTorch', 2, 'Language understanding model for chat-based tasks.'),
('StockAI', 'Time Series Forecasting', 'Keras', 3, 'Predicts stock trends using LSTM layers.'),
('DeepScan', 'Medical Imaging', 'TensorFlow', 4, 'Detects tumors in MRI scans.'),
('DriveAI', 'Autonomous Driving', 'PyTorch', 5, 'Real-time object detection for vehicles.'),
('SentimentX', 'Sentiment Analysis', 'Keras', 6, 'Analyzes emotions in text data.'),
('VoiceNet', 'Speech Recognition', 'TensorFlow', 7, 'Transcribes audio with high accuracy.'),
('GenAI', 'Text Generation', 'PyTorch', 8, 'GPT-based model for content creation.'),
('VisionPro', 'Object Detection', 'TensorFlow', 9, 'YOLO-based model for industrial inspection.'),
('RoboMind', 'Reinforcement Learning', 'Keras', 10, 'RL agent for robotic path optimization.');

-- Model version
INSERT INTO Model_Version (Model_ID, Version, Changes, Date_Created) VALUES
(1, 'v1.1', 'Improved CNN layers and added data augmentation', '2024-02-15'),
(2, 'v2.0', 'Upgraded tokenizer and added transformer heads', '2024-03-12'),
(3, 'v1.3', 'Added dropout and fine-tuned LSTM parameters', '2024-04-05'),
(4, 'v1.2', 'Enhanced preprocessing and added extra MRI filters', '2024-05-18'),
(5, 'v3.0', 'Integrated YOLOv8 and optimized real-time detection', '2024-06-09'),
(6, 'v1.5', 'Added attention mechanism for better sentiment capture', '2024-07-20'),
(7, 'v2.2', 'Improved audio normalization and sequence labeling', '2024-08-14'),
(8, 'v3.1', 'Fine-tuned GPT layers and improved sampling diversity', '2024-09-28'),
(9, 'v1.4', 'Integrated transfer learning for better object detection', '2024-10-15'),
(10, 'v2.0', 'Reinforced exploration strategy in RL agent', '2024-11-01');

-- 🧩 Dataset (10)
INSERT INTO Dataset (Name, Source, Type, Size_GB, License) VALUES
('ImageNet', 'https://image-net.org', 'Image', 150.5, 'MIT'),
('ChatCorpus', 'https://huggingface.co/chat', 'Text', 12.8, 'Apache 2.0'),
('StockMarket2024', 'https://data.yfinance.com', 'CSV', 4.3, 'CC-BY 4.0'),
('MRI_Scan_Set', 'https://medicaldata.org/mri', 'Image', 85.0, 'OpenML'),
('DriveFootage', 'https://autovision.ai/data', 'Video', 250.2, 'GPLv3'),
('EmotionTweets', 'https://huggingface.co/emotion', 'Text', 9.5, 'MIT'),
('SpeechDataPro', 'https://openslr.org/60', 'Audio', 35.2, 'CC-BY 4.0'),
('CreativeText', 'https://genai.tech/data', 'Text', 22.1, 'Apache 2.0'),
('InspectionImages', 'https://industrydata.io', 'Image', 60.7, 'MIT'),
('RobotSim', 'https://robotics.ai/sim', 'CSV', 5.4, 'GPLv2');

-- ⚙️ Training (25 runs total — multiple per model)
INSERT INTO Training (Model_ID, Dataset_ID, Epochs, Batch_Size, Learning_Rate, Optimizer) VALUES
-- VisionNet
(1, 1, 25, 32, 0.001, 'Adam'),
(1, 1, 30, 64, 0.0008, 'RMSProp'),
(1, 9, 20, 32, 0.0012, 'Adam'),
-- ChatBrain
(2, 2, 15, 16, 0.0005, 'AdamW'),
(2, 6, 18, 32, 0.0007, 'Adam'),
(2, 8, 20, 32, 0.0006, 'RMSProp'),
-- StockAI
(3, 3, 30, 64, 0.002, 'RMSProp'),
(3, 3, 28, 32, 0.0015, 'Adam'),
-- DeepScan
(4, 4, 20, 32, 0.001, 'SGD'),
(4, 4, 25, 32, 0.0009, 'Adam'),
(4, 1, 22, 64, 0.0011, 'RMSProp'),
-- DriveAI
(5, 5, 40, 16, 0.0007, 'Adam'),
(5, 5, 42, 32, 0.0006, 'RMSProp'),
-- SentimentX
(6, 6, 25, 64, 0.001, 'Adam'),
(6, 2, 20, 32, 0.0012, 'AdamW'),
(6, 8, 30, 16, 0.0009, 'RMSProp'),
-- VoiceNet
(7, 7, 30, 32, 0.0009, 'RMSProp'),
(7, 7, 35, 32, 0.0008, 'Adam'),
-- GenAI
(8, 8, 18, 16, 0.0004, 'AdamW'),
(8, 8, 22, 32, 0.0005, 'Adam'),
-- VisionPro
(9, 9, 28, 32, 0.001, 'Adam'),
(9, 9, 32, 64, 0.0012, 'RMSProp'),
-- RoboMind
(10, 10, 35, 64, 0.002, 'SGD'),
(10, 10, 38, 32, 0.0015, 'Adam'),
(10, 3, 30, 64, 0.002, 'RMSProp');

-- ⚙️ Parameter (1 per training)
INSERT INTO Parameter (Training_ID, Name, Value) VALUES
(1, 'Dropout Rate', '0.4'),
(2, 'Dropout Rate', '0.3'),
(3, 'Dropout Rate', '0.5'),
(4, 'Sequence Length', '512'),
(5, 'Sequence Length', '256'),
(6, 'Sequence Length', '768'),
(7, 'Lookback Window', '60'),
(8, 'Lookback Window', '90'),
(9, 'Momentum', '0.9'),
(10, 'Momentum', '0.8'),
(11, 'Momentum', '0.85'),
(12, 'Learning Decay', '0.0001'),
(13, 'Learning Decay', '0.0002'),
(14, 'Embedding Size', '256'),
(15, 'Embedding Size', '512'),
(16, 'Embedding Size', '768'),
(17, 'Noise Reduction', 'True'),
(18, 'Noise Reduction', 'False'),
(19, 'Top-k Sampling', '50'),
(20, 'Top-p Sampling', '0.9'),
(21, 'Confidence Threshold', '0.6'),
(22, 'Confidence Threshold', '0.7'),
(23, 'Reward Factor', '0.75'),
(24, 'Reward Factor', '0.8'),
(25, 'Reward Factor', '0.65');

-- Hardware Congifuration
INSERT INTO Hardware_Config (Training_ID, GPU_Type, CPU_Type, Ram) VALUES
(1, 'NVIDIA RTX 3090', 'Intel i9-12900K', '64GB'),
(2, 'NVIDIA RTX 4090', 'AMD Ryzen 9 7950X', '128GB'),
(3, 'NVIDIA RTX 3080', 'Intel i7-12700K', '32GB'),
(4, 'NVIDIA A100', 'AMD EPYC 7502', '256GB'),
(5, 'NVIDIA RTX 4070 Ti', 'Intel i9-11900K', '64GB'),
(6, 'NVIDIA RTX 3060 Ti', 'Intel i5-12600K', '32GB'),
(7, 'NVIDIA RTX 3090', 'AMD Ryzen 7 5800X', '64GB'),
(8, 'NVIDIA RTX 3080 Ti', 'Intel i9-12900K', '64GB'),
(9, 'NVIDIA Tesla V100', 'AMD EPYC 7452', '128GB'),
(10, 'NVIDIA RTX 3090', 'Intel Xeon W-2295', '128GB'),
(11, 'NVIDIA A6000', 'AMD Threadripper PRO 5975WX', '256GB'),
(12, 'NVIDIA RTX 4090', 'Intel i9-13900K', '128GB'),
(13, 'NVIDIA RTX 4070', 'AMD Ryzen 9 5900X', '64GB'),
(14, 'NVIDIA RTX 3080', 'Intel i7-11700K', '32GB'),
(15, 'NVIDIA RTX 3060', 'Intel i5-12400F', '32GB'),
(16, 'NVIDIA RTX 4070 Ti', 'Intel i9-11900K', '64GB'),
(17, 'NVIDIA RTX 3090', 'AMD Ryzen 9 7950X', '128GB'),
(18, 'NVIDIA RTX 3080 Ti', 'Intel i9-12900K', '64GB'),
(19, 'NVIDIA RTX 4070', 'AMD Ryzen 7 5800X', '32GB'),
(20, 'NVIDIA A100', 'AMD EPYC 7502', '256GB'),
(21, 'NVIDIA RTX 4090', 'Intel i9-13900K', '128GB'),
(22, 'NVIDIA RTX 3080', 'Intel i7-11700K', '32GB'),
(23, 'NVIDIA Tesla V100', 'AMD EPYC 7452', '128GB'),
(24, 'NVIDIA RTX 4070 Ti', 'Intel i9-11900K', '64GB'),
(25, 'NVIDIA RTX 3090', 'Intel i9-12900K', '64GB');

-- 📊 Performance (linked to each training)
INSERT INTO Performance (Training_ID, Accuracy, Model_Precision, Recall, F1_Score, Loss, Training_Time)
VALUES
(1, 0.95, 0.94, 0.93, 0.935, 0.12, '00:25:30'),
(2, 0.89, 0.87, 0.88, 0.875, 0.25, '00:32:15'),
(3, 0.91, 0.90, 0.89, 0.895, 0.98, '00:28:45'),
(4, 0.78, 0.80, 0.76, 0.78, 0.45, '00:40:10'),
(5, 0.96, 0.95, 0.94, 0.945, 0.10, '00:20:50'),
(6, 0.84, 0.83, 0.82, 0.825, 0.33, '00:35:22'),
(7, 0.12, 0.91, 0.90, 0.905, 0.16, '00:24:11'),
(8, 0.88, 0.86, 0.87, 0.865, 0.28, '00:31:50'),
(9, 0.75, 0.77, 0.74, 0.755, 0.52, '00:42:40'),
(10, 0.98, 0.97, 0.96, 0.965, 0.08, '00:19:55'),
(11, 0.81, 0.82, 0.79, 0.805, 0.39, '00:37:33'),
(12, 0.94, 0.93, 0.92, 0.925, 0.14, '00:26:20'),
(13, 0.87, 0.85, 0.84, 0.845, 0.31, '00:30:14'),
(14, 0.20, 0.88, 0.89, 0.885, 0.20, '00:29:44'),
(15, 0.97, 0.96, 0.95, 0.955, 0.09, '00:21:08'),
(16, 0.79, 0.80, 0.78, 0.79, 0.47, '00:41:00'),
(17, 0.85, 0.84, 0.83, 0.835, 0.96, '00:34:18'),
(18, 0.93, 0.92, 0.91, 0.915, 0.15, '00:27:45'),
(19, 0.32, 0.81, 0.80, 0.805, 0.38, '00:36:55'),
(20, 0.99, 0.98, 0.97, 0.975, 0.05, '00:18:22'),
(21, 0.76, 0.78, 0.75, 0.765, 0.49, '00:43:09'),
(22, 0.91, 0.89, 0.88, 0.885, 0.19, '00:28:00'),
(23, 0.83, 0.82, 0.81, 0.815, 0.37, '00:33:41'),
(24, 0.95, 0.94, 0.93, 0.935, 0.11, '00:23:57'),
(25, 0.38, 0.87, 0.86, 0.865, 0.87, '00:30:45');

