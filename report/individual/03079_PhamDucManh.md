# Báo cáo cá nhân — PhamDucManh-03079

Đổi tên file theo quy tắc `MSSV_HoTen.md`. Ví dụ: `03079_PhamDucManh.md`.

Dữ liệu: 12 ảnh người COCO val2017 (Lin et al., 2014) và 8 ảnh chân dung Wikimedia Commons, chỉ dùng trong lớp.

## 0. Thông tin học viên

- Họ tên: Phạm Đức Mạnh
- MSSV: 03079
- Email: manh.pham03079@gmail.com
- Link repository: https://github.com/manhpd03079/K5-L2-DAY04-PhamDucManh-03079-KeypointPose
- Phiên bản CVAT (Help → About): 2.74.1
- Máy: hệ điều hành Windows 10/11 · RAM 8 GB · chạy CVAT chế độ lite
- Bộ ảnh (`src/exports/assignment.json` do `lab.py setup` tạo): có
- Giờ bắt đầu: 17:15
- Giờ kết thúc: 19:15

## 1. Kiểm tra label (CP0)

| Label | Kiểu | Số điểm | Tên điểm đúng bảng của lab? | Đúng thứ tự? | Số cạnh |
|---|---|---:|---|---|---:|
| `person` | Skeleton | 17 | Có | Có | 19 |
| `face` | Skeleton | 13 | Có | Có | 13 |

Mẫu `person` dựng theo người quay mặt về camera (các điểm `left_*` nằm bên phải khung mẫu)? Có

Cách đổi cờ `occluded` / `outside` cho **một điểm** trên phiên bản CVAT này (một câu):
Rê chuột vào đúng điểm cần đổi cho điểm sáng lên, bấm phím `Q` để bật/tắt `occluded` (v = 1) hoặc phím `O` để bật/tắt `outside` (v = 0), hoặc click chuột phải vào điểm để chọn menu cờ.

## 2. Số lượng đã gán và thời gian (CP1, CP2)

| Nhóm ảnh | Số ảnh | Số skeleton đã gán | Số người dưới 60 px (không gán) | Số poster / gương / màn hình bỏ qua | Thời gian (phút) |
|---|---:|---:|---:|---:|---:|
| `easy` | 5 | 5 | 0 | 0 | 25 |
| `occluded` | 3 | 6 | 0 | 0 | 20 |
| `back` | 2 | 4 | 0 | 0 | 18 |
| `small` | 1 | 2 | 1 | 0 | 10 |
| `crowd` | 1 | 3 | 2 | 0 | 15 |
| `faces` | 8 | 8 | — | 0 | 25 |

- Số ảnh người đã xong ở mốc phút 105: 10 / 10
- Thời gian thực tế (phút): CP1 73 · CP2 25 · CP3 15
- Ảnh tốn thời gian nhất là ảnh nào, vì sao?
Ảnh `000000309169.jpg` (nhóm crowd) tốn nhiều thời gian nhất vì có nhiều người đứng gần nhau, các chi bị che khuất và chồng chéo, phải lần theo từng khớp từ vai → khuỷu → cổ tay của từng người để tránh nối nhầm xương sang người khác.

## 3. Bảng ca khó (CP1, CP2)

Mỗi điểm bạn phân vân một dòng, nhất là phân vân giữa `v = 1` và `v = 0`, hoặc không chắc hướng người.

| Ảnh | Người / mặt | Điểm | Cờ đã chọn | Phân vân giữa | Lý do chọn |
|---|---|---|---:|---|---|
| `000000056651.jpg` | Người #1 | `left_ankle`, `right_ankle` | 0 | v = 1 và v = 0 | Chân bị cắt ngang mép dưới của ảnh, phần khớp cổ chân nằm ngoài khung ảnh nên chọn outside (v = 0) theo đúng quy tắc |
| `000000069971.jpg` | Cầu thủ #32 | `nose`, `left_eye`, `right_eye` | 0 | v = 1 và v = 0 | Người quay lưng hoàn toàn về phía camera, không thể ước lượng chính xác vị trí mắt mũi nên chọn outside (v = 0) |
| `000000516902.jpg` | Người trong xe | `left_knee`, `left_ankle` | 1 | v = 1 và v = 0 | Chân bị cửa xe che nhưng dựa theo tư thế ngồi và hướng hông/đùi có thể ước lượng chắc chắn vị trí gối |
| `face_405456.jpg` | Mặt kính râm | 4 điểm quanh mắt | 1 | v = 1 và v = 2 | Tròng kính râm tối che khuất con ngươi và mí mắt nhưng đoán được vị trí mắt dựa theo khung gọng kính |

## 4. Bảng tự review (CP3)

Đi từ ảnh cuối về ảnh đầu. 5 ảnh người (ít nhất 2 ảnh `back` hoặc `crowd`) và 3 ảnh mặt. Ít nhất 8 dòng, kể cả dòng `ok`. Ghi lỗi trước, sửa sau.

Mã lỗi dùng đúng một trong: `lr_swap`, `vis_flag`, `position`, `missing`, `extra`, `ok`.

| Ảnh | Người / mặt | Điểm | Mã lỗi | Ghi chú | Đã sửa? |
|---|---|---|---|---|---|
| `000000309169.jpg` | Người #1, #2, #3 | Toàn thân | `ok` | Nhóm crowd đã gán đủ 3 người chính ≥ 60 px, không sót người | Đã kiểm tra |
| `000000163118.jpg` | Người nhảy #76 | `wrist`, `ankle` | `ok` | Tư thế nhảy bắt đĩa bay chân tay bắt chéo tự nhiên trong không gian, đã kiểm tra đúng vai → khuỷu → cổ tay | Đã kiểm tra |
| `000000069971.jpg` | Cầu thủ quay lưng | `left_eye`, `right_eye` | `vis_flag` | Ban đầu để v = 2 theo mẫu, sửa sang outside (v = 0) vì quay lưng không thấy mặt | Có |
| `000000056651.jpg` | Người #1 | `left_ankle`, `right_ankle` | `vis_flag` | Điểm ngoài ảnh bị đặt v = 1, sửa thành outside (v = 0) bằng phím O | Có |
| `000000056651.jpg` | Người #2 | `left_ankle` | `vis_flag` | Điểm ngoài ảnh ban đầu để v = 2, sửa thành outside (v = 0) | Có |
| `face_41666.jpg` | Mặt #1 | Toàn mặt | `ok` | Khóe mắt, mí mắt và môi đặt chuẩn mép, đúng trái phải | Đã kiểm tra |
| `face_405456.jpg` | Mặt kính râm | `left_eye_*`, `right_eye_*` | `vis_flag` | Kính râm che mắt, chuyển cờ 4 điểm mắt sang occluded (v = 1) | Có |
| `face_125051.jpg` | Mặt thẳng | `left_eye_upper` | `position` | Mí mắt trên bị lệch 2 px lên lông mày, đã kéo lại đúng mép mí trên con ngươi | Có |

Tổng hợp số lỗi theo mã:

| `lr_swap` | `vis_flag` | `position` | `missing` | `extra` | `ok` |
|---:|---:|---:|---:|---:|---:|
| 0 | 4 | 1 | 0 | 0 | 3 |

Điểm còn phân vân giữa `v = 1` và `v = 0` (ghi cả hai lựa chọn và lý do chọn):
Tại ảnh `000000056651.jpg`, hai cổ chân của người đứng bị mép dưới khung ảnh cắt ngang. Nếu chọn v = 1 thì model sẽ bị phạt vì học điểm ngoài biên; chọn v = 0 (outside) là chính xác theo guideline vì điểm nằm ngoài khung hình không được đoán bừa.

## 5. Kiểm file xuất và kết quả tự kiểm (CP4)

Tự kiểm tay trong file JSON:

| File | Người / mặt kiểm (ảnh, thứ tự) | Số phần tử `keypoints` | Điểm `outside` ra `v = 0`, `occluded` ra `v = 1`? | `num_keypoints` khớp? |
|---|---|---:|---|---|
| `PhamDucManh_persons.zip` | `000000056651.jpg` (#1) | 51 | Có | Có (khớp 15 điểm v > 0) |
| `PhamDucManh_persons.zip` | `000000069971.jpg` (#1) | 51 | Có | Có (khớp 8 điểm v > 0) |
| `PhamDucManh_faces.zip` | `face_125051.jpg` (#1) | 39 | Có | Có (khớp 13 điểm v > 0) |

Sau khi xuất, CVAT ghi `occluded` thành `v = 1` và `outside` thành `v = 0`. Tọa độ của điểm `outside` trong file là `0, 0` hay tọa độ cũ? Tọa độ cũ (CVAT 2.x giữ nguyên tọa độ cũ, điểm v = 0 sẽ tự động bị bỏ qua khi tính loss và OKS).

Hai job đã chuyển sang completed trên CVAT? Có

Dán phần **TÓM TẮT** in ra từ `src/check_submission.py`:

```text
----- TÓM TẮT (dán vào báo cáo mục 5) -----
- File person: PhamDucManh_persons.zip
  Số ảnh: 12 · số skeleton `person`: 20 · mỗi annotation 51 số
  Skeleton theo ảnh: 000000056651=2, 000000069971=2, 000000072098=1, 000000150192=2, 000000163118=2, 000000177889=1, 000000196283=1, 000000309169=3, 000000455536=1, 000000461389=3, 000000516902=1, 000000525227=1
  Cờ v: v=2 264 (78%) · v=1 19 (6%) · v=0 57 (17%)
  num_keypoints trung bình: 14.2
- File face: PhamDucManh_faces.zip
  Số ảnh: 8 · số skeleton `face`: 8 · mỗi annotation 39 số
  Skeleton theo ảnh: face_125051=1, face_145621=1, face_155465=1, face_405456=1, face_41666=1, face_442231=1, face_556064=1, face_575921=1
  Cờ v: v=2 99 (95%) · v=1 5 (5%) · v=0 0 (0%)
  num_keypoints trung bình: 13.0
- Ghi chú: 57 điểm v = 0 vẫn mang tọa độ cũ (CVAT 2.x xuất như vậy; chuẩn COCO ghi 0, 0). Không phải lỗi: điểm v = 0 bị bỏ qua khi huấn luyện và khi chấm.
- Số [LỖI]: 0 · số [CẢNH BÁO]: 4
Kết quả: ĐẠT (đọc lại từng cảnh báo ở trên)
```

Các `[CẢNH BÁO]` còn giữ nguyên và lý do:
Có 4 cảnh báo về cặp wrist / ankle nằm ngược phía ở các ảnh `000000056651.jpg`, `000000163118.jpg`, `000000455536.jpg`. Lý do giữ nguyên: Người trong ảnh đang thực hiện động tác khoanh tay, vắt tay qua người hoặc nhảy bắt đĩa frisbee trên không dẫn đến tay/chân bắt chéo thật so với trục cơ thể. Đã kiểm tra kỹ các đường nối chi khớp (vai → khuỷu → cổ tay, hông → gối → cổ chân) hoàn toàn chính xác theo đúng giải phẫu cơ thể người trong ảnh, không bị đảo trái/phải (`lr_swap`).

## 6. Ảnh chụp màn hình

1. Label `person` trong label constructor (đủ 17 điểm có tên):

   ![Label person](images/1_label_person.png)

2. Một người quay lưng đã gán, cờ đã đặt:

   ![Người quay lưng](images/2_nguoi_quay_lung.png)

3. Một khuôn mặt đã gán 13 điểm, phóng to vùng mắt:

   ![Khuôn mặt phóng to](images/3_mat_phong_to.png)

4. Một đoạn JSON xuất của một người:

   ![JSON export](images/4_json_export.png)

Nguồn ảnh: COCO val2017 / Wikimedia Commons.

## 7. Tự đánh giá

1. Lỗi bạn mắc nhiều nhất hôm nay, và cách bạn sẽ tránh ở dự án thật:
Lỗi hay mắc nhất là quên bật cờ `outside` cho các điểm khớp nằm ngoài biên ảnh (để v = 1 hoặc v = 2), và dễ nhầm trái/phải khi người quay lưng. Cách tránh: Luôn xác định hướng người (quay mặt hay quay lưng) trước khi kéo điểm, và kiểm tra 4 câu hỏi visibility cho từng điểm trước khi lưu.

2. Một quy tắc bạn đề xuất thêm vào guideline (kèm ảnh ví dụ nếu có):
Đề xuất bổ sung quy định rõ ràng về ngưỡng dung sai khi gán keypoint khớp hông qua quần áo thụng/váy xòe: nên quy định ước lượng dựa trên đường trục cột sống và khớp đùi đối xứng để các annotator có cùng một chuẩn ước lượng thống nhất.

3. Nhãn của bạn đi vào model ở đâu? Chọn một lỗi bạn đã sửa và nói nó sẽ làm model học sai thế nào (heatmap, trọng số trong loss, hay bước lật ảnh):
Nhãn keypoint đi vào model để tạo các ground-truth heatmaps 2D (Gaussian peak tại mỗi vị trí khớp có v > 0). Ví dụ lỗi đặt điểm ngoài ảnh thành v = 1: model sẽ tạo một đỉnh heatmap giả ở vị trí đó và tính loss, khiến model học đoán mò các điểm ngoài khung hình. Hoặc nếu bị lỗi `lr_swap`, bước data augmentation lật ảnh (horizontal flip) sẽ tráo nhầm tên các khớp đối xứng, phá hỏng khả năng học đặc trưng của model.

## 8. Khó khăn và lỗi kỹ thuật

- Ban đầu gặp lỗi không gọi được Docker do Docker Engine chưa khởi động hoàn tất, đã xử lý bằng cách mở Docker Desktop chờ trạng thái `Engine running`.
- Quên mật khẩu đăng nhập tài khoản CVAT ngày 2, đã sử dụng lệnh `python3 ~/manage.py changepassword` trong container `cvat_server` để thiết lập lại mật khẩu thành công.
- Đã chạy chế độ `python lab.py lite` để tối ưu RAM cho máy trong suốt quá trình gán nhãn.

## 9. Tài liệu tham khảo và công cụ AI đã dùng

- Hướng dẫn chuẩn COCO Keypoints và quy tắc gán nhãn trong repo (`docs/GUIDELINE.md`, `docs/CVAT_CHEATSHEET.md`).
- Trợ lý AI Antigravity: hỗ trợ tra cứu nguyên nhân cảnh báo `check_submission.py`, kiểm tra cú pháp lệnh PowerShell và định dạng báo cáo.
