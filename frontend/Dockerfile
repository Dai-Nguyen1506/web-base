# Stage 1: Build the React Application
FROM node:18-alpine as builder

WORKDIR /app

# Khởi tạo package.json và cài đặt dependencies (bạn cần chạy 'npm install' ở local trước để có package-lock.json)
# Nếu bạn chưa có package-lock.json, lệnh npm install bên dưới sẽ tự tạo.
COPY package.json ./
RUN npm install

# Copy toàn bộ mã nguồn vào container
COPY . .

# Build ứng dụng Vite/React ra thư mục 'dist'
RUN npm run build

# Stage 2: Serve bằng Nginx
FROM nginx:alpine

# Copy thư mục build từ stage 1 sang Nginx
COPY --from=builder /app/dist /usr/share/nginx/html

# Cấu hình Nginx mặc định (để hỗ trợ React Router)
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
