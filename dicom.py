import pydicom as dm
import matplotlib.pyplot as plt
import numpy as np

path = dm.data.get_testdata_file("CT_small.dcm")
file = dm.dcmread(path)

def visualize_1(dicom_file, show=True):
    file = dm.dcmread(dicom_file)
    image = file.pixel_array.astype(float)

    print(f"max = {image.max()}, min = {image.min()}")

    normalized_image = (image - image.min()) / (image.max() - image.min())
    normalized_image = normalized_image * 255.0

    unit8_image = np.round(normalized_image).astype(np.uint8)

    if show:
        plt.imshow(unit8_image, cmap="gray")
        plt.title("Min-Max Normalized")
        plt.show()

    return unit8_image

def visualize_2(dicom_file, show=True, p=None, n=None):
    file = dm.dcmread(dicom_file)
    image = file.pixel_array.astype(float)

    if p is None:
        p = image.max()

    if n is None:
        n = image.min()

    clipped_image = np.clip(image, n, p)

    normalized = ((clipped_image - n) / (p - n)) * 255.0

    normalized_unit8 = np.round(normalized).astype(np.uint8)

    if show:
        plt.imshow(normalized_unit8, cmap="gray")
        plt.title(f"Window: {n} to {p}")
        plt.show()

    return normalized_unit8

# الدالة الأولى:
# إذا دخل المستخدم قيمة تتغير، وإذا ما دخل تبقى الأصلية
def change_tags(
    path,
    output_path,
    patient_name=None,
    patient_id=None,
    birth_date=None,
    sex=None,
    age=None,
    address=None,
    institution=None,
    physician=None,
    study_date=None,
    accession_number=None
):
    file = dm.dcmread(path)

    if patient_name:
        file.PatientName = patient_name

    if patient_id:
        file.PatientID = patient_id

    if birth_date:
        file.PatientBirthDate = birth_date

    if sex:
        file.PatientSex = sex

    if age:
        file.PatientAge = age

    if address:
        file.PatientAddress = address

    if institution:
        file.InstitutionName = institution

    if physician:
        file.ReferringPhysicianName = physician

    if study_date:
        file.StudyDate = study_date

    if accession_number:
        file.AccessionNumber = accession_number

    file.save_as(output_path)

    return output_path

# الدالة الثانية:
# إذا دخل المستخدم قيمة تتغير، وإذا ما دخل تصير فاضية
def anonymize_file(
    path,
    output_path,
    patient_name=None,
    patient_id=None,
    birth_date=None,
    sex=None,
    age=None,
    address=None,
    institution=None,
    physician=None,
    study_date=None,
    accession_number=None
):
    file = dm.dcmread(path)

    if patient_name:
        file.PatientName = patient_name
    else:
        file.PatientName = ""

    if patient_id:
        file.PatientID = patient_id
    else:
        file.PatientID = ""

    if birth_date:
        file.PatientBirthDate = birth_date
    else:
        file.PatientBirthDate = ""

    if sex:
        file.PatientSex = sex
    else:
        file.PatientSex = ""

    if age:
        file.PatientAge = age
    else:
        file.PatientAge = ""

    if address:
        file.PatientAddress = address
    else:
        file.PatientAddress = ""

    if institution:
        file.InstitutionName = institution
    else:
        file.InstitutionName = ""

    if physician:
        file.ReferringPhysicianName = physician
    else:
        file.ReferringPhysicianName = ""

    if study_date:
        file.StudyDate = study_date
    else:
        file.StudyDate = ""

    if accession_number:
        file.AccessionNumber = accession_number
    else:
        file.AccessionNumber = ""

    file.save_as(output_path)

    return output_path

# عرض الصور
image_1 = visualize_1(path, show=True)
image_2 = visualize_2(path, show=True, p=1700.0, n=300.0)

# طباعة معلومات الملف الأصلي
print(file)

# مثال 1: تغيير بعض القيم فقط، والباقي يبقى أصلي
new_path_1 = change_tags(
    path,
    "CT_changed_tags.dcm",
    patient_name="Anonymous",
    patient_id="ANON-001",
    sex="M"
)

new_file_1 = dm.dcmread(new_path_1)

print("Patient Name:", new_file_1.PatientName)
print("Patient ID:", new_file_1.PatientID)
print("Birth Date:", new_file_1.PatientBirthDate)
print("Sex:", new_file_1.PatientSex)
print("Institution:", new_file_1.get("InstitutionName", "Not available"))

# مثال 2: تغيير بعض القيم، والباقي يصير فاضي
new_path_2 = anonymize_file(
    path,
    "CT_anonymized.dcm",
    patient_name="Anonymous",
    patient_id="ANON-001",
    sex="M"
)

new_file_2 = dm.dcmread(new_path_2)

print("Patient Name:", new_file_2.PatientName)
print("Patient ID:", new_file_2.PatientID)
print("Birth Date:", new_file_2.PatientBirthDate)
print("Sex:", new_file_2.PatientSex)
print("Institution:", new_file_2.get("InstitutionName", "Not available"))
