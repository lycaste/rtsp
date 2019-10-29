MatOfRect faceDetections = new MatOfRect();
        faceDetector.detectMultiScale(image, faceDetections);

        System.out.println(String.format("Detected %s faces", faceDetections.toArray().length));
        Point center = null;
        int radius = 200;
        for (Rect rect : faceDetections.toArray()) {
            center = new Point(rect.x +  (int) (rect.width/2),rect.y+(int)(rect.height/2));
        }
        Mat c = Mat.zeros(image.rows(), image.cols(), CvType.CV_8UC4);


        for (int x = 0; x < image.cols(); x++) {
            for (int y= 0; y < image.rows(); y++) {
                double temp = ((x - center.x) * (x - center.x) + (y - center.y) *(y - center.y));
                if (temp < (radius * radius)) {
                    double[] re = new double[4];
                    re[0]= image.get(y,x)[0];
                    re[1]= image.get(y,x)[1];
                    re[2]= image.get(y,x)[2];
                    re[3]= 255;

                    c.put(y,x,re);
                }

            }
        }

        String filename1 = "faceDetection1.png";
        Imgcodecs.imwrite(filename1, c);
