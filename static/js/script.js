const navContainer = document.getElementById('nav-container');
const navItems = navContainer.querySelectorAll('.nav-item');
console.log(navItems);
const parameterBox = document.getElementById('parameter-box');
const imageContainer = document.getElementById('image-container');
const imageShower = document.getElementById('image-shower');
const uploadForm = document.getElementById('upload-form');
const imageInput = document.getElementById('image-input');

imageContainer.style.width = (window.innerWidth - 20) + 'px';
imageContainer.style.height = (window.innerHeight - 250) + 'px';

const originParameter = `
<form id="upload-form">
    <input type="file" id="image-input" accept=".png, .jpg, .jpeg" />
<button type="submit">上传</button>
`;

const edgeParameter = `
<ul>
    <p>线条粗细</p>
    <input type="text" placeholder="5" id="arg1">
</ul>
<ul>
    <p>滤波大小</p>
    <input type="text" placeholder="7" id="arg2">
</ul>
<ul>
    <button id="start-button">开始转换</button>
</ul>
`;

const lineParameter = `
<ul>
    <p>线条粗细</p>
    <input type="text" placeholder="2" id="arg1">
</ul>
<ul>
    <p>密度缩放大小（越大越密）</p>
    <input type="text" placeholder="0.1" id="arg2">
</ul>
<ul>
    <p>块大小</p>
    <input type="text" placeholder="48" id="arg3">
</ul>
<ul>
    <button id="start-button">开始转换</button>
</ul>
`;

const dotParameter = `
<ul>
    <p>点大小</p>
    <input type="text" placeholder="3" id="arg1">
</ul>
<ul>
    <p>密度缩放大小（越大越密）</p>
    <input type="text" placeholder="0.1" id="arg2">
</ul>
<ul>
    <p>块大小</p>
    <input type="text" placeholder="48" id="arg3">
</ul>
<ul>
    <p>最小点密度（小于不显示）</p>
    <input type="text" placeholder="0.1" id="arg4">
</ul>
<ul>
    <button id="start-button">开始转换</button>
</ul>
`;

const combineParameter = `
<ul>
    <select name="type" id="select">
        <option value="N">线图</option>
        <option value="Y">点图</option>
    </select>
</ul>
<ul>
    <button id="start-button">开始转换</button>
</ul>
`;

navItems.forEach(item => {
    item.addEventListener('click', () => {
        if (item.classList.contains('origin')) {
            parameterBox.innerHTML = originParameter;
            imageShower.src = "./get_image";
            imageShower.alt = "原图";
        } else if (item.classList.contains('edge')) {
            parameterBox.innerHTML = edgeParameter;
            imageShower.src = "./get_edge";
            imageShower.alt = "线稿";
            const startButton = parameterBox.querySelector('#start-button');
            startButton.addEventListener('click', async () => {
                let arg1 = parameterBox.querySelector('#arg1').value;
                let arg2 = parameterBox.querySelector('#arg2').value;
                if (arg1 === '') {
                    arg1 = '5';
                }
                if (arg2 === '') {
                    arg2 = '7';
                }
                console.log(arg1, arg2);
                // 调用 API 转换图片
                try {
                    const response = await fetch('http://127.0.0.1:5145/run_edge', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                            arg1,
                            arg2,
                        }),
                    });

                    if (response.ok) {
                        const result = response.json(); // 解析 JSON 响应
                        console.log('图片转换成功:', result);
                        // 显示转换后的图片
                        imageShower.src = "./get_edge";
                        imageShower.alt = "线稿";
                        location.reload(); // 刷新页面
                    } else {
                        console.error('转换失败:', response.statusText);
                    }
                } catch (error) {
                    console.error('请求错误:', error);
                }
            });
        } else if (item.classList.contains('line')) {
            parameterBox.innerHTML = lineParameter;
            imageShower.src = "./get_line";
            imageShower.alt = "线画";
            const startButton = parameterBox.querySelector('#start-button');
            startButton.addEventListener('click', async () => {
                let arg1 = parameterBox.querySelector('#arg1').value;
                let arg2 = parameterBox.querySelector('#arg2').value;
                let arg3 = parameterBox.querySelector('#arg3').value;
                if (arg1 === '') {
                    arg1 = '2';
                }
                if (arg2 === '') {
                    arg2 = '0.1';
                }
                if (arg3 === '') {
                    arg3 = '48';
                }
                console.log(arg1, arg2, arg3);
                // 调用 API 转换图片
                try {
                    const response = await fetch('http://127.0.0.1:5145/run_line', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                            arg1,
                            arg2,
                            arg3,
                        }),
                    });

                    if (response.ok) {
                        const result = response.json(); // 解析 JSON 响应
                        console.log('图片转换成功:', result);
                        // 显示转换后的图片
                        imageShower.src = "./get_line";
                        imageShower.alt = "线画";
                        location.reload(); // 刷新页面
                    } else {
                        console.error('转换失败:', response.statusText);
                    }
                } catch (error) {
                    console.error('请求错误:', error);
                }
            });
        } else if (item.classList.contains('dot')) {
            parameterBox.innerHTML = dotParameter;
            imageShower.src = "./get_dot";
            imageShower.alt = "点画";
            const startButton = parameterBox.querySelector('#start-button');
            startButton.addEventListener('click', async () => {
                let arg1 = parameterBox.querySelector('#arg1').value;
                let arg2 = parameterBox.querySelector('#arg2').value;
                let arg3 = parameterBox.querySelector('#arg3').value;
                let arg4 = parameterBox.querySelector('#arg4').value;
                if (arg1 === '') {
                    arg1 = '3';
                }
                if (arg2 === '') {
                    arg2 = '0.1';
                }
                if (arg3 === '') {
                    arg3 = '48';
                }
                if (arg4 === '') {
                    arg4 = '0.1';
                }
                console.log(arg1, arg2, arg3, arg4);
                // 调用 API 转换图片
                try {
                    const response = await fetch('http://127.0.0.1:5145/run_dot', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                            arg1,
                            arg2,
                            arg3,
                            arg4,
                        }),
                    });

                    if (response.ok) {
                        const result = response.json(); // 解析 JSON 响应
                        console.log('图片转换成功:', result);
                        // 显示转换后的图片
                        imageShower.src = "./get_dot";
                        imageShower.alt = "点画";
                        location.reload(); // 刷新页面
                    } else {
                        console.error('转换失败:', response.statusText);
                    }
                } catch (error) {
                    console.error('请求错误:', error);
                }
            });
        } else if (item.classList.contains('combine')) {
            parameterBox.innerHTML = combineParameter;
            imageShower.src = "./get_combine";
            imageShower.alt = "混合画";
            const select = parameterBox.querySelector('#select');
            const startButton = parameterBox.querySelector('#start-button');
            startButton.addEventListener('click', async () => {
                let type = select.value;
                console.log(type);
                // 调用 API 转换图片
                try {
                    const response = await fetch('http://127.0.0.1:5145/run_combine', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                            type,
                        }),
                    });

                    if (response.ok) {
                        const result = response.json(); // 解析 JSON 响应
                        console.log('图片转换成功:', result);
                        // 显示转换后的图片
                        imageShower.src = "./get_combine";
                        imageShower.alt = "混合画";
                        location.reload(); // 刷新页面
                    } else {
                        console.error('转换失败:', response.statusText);
                    }
                } catch (error) {
                    console.error('请求错误:', error);
                }
            });
        }
    });
});

uploadForm.addEventListener('submit', async function(event) {
    event.preventDefault(); // 阻止表单默认提交

    const file = imageInput.files[0]; // 获取上传的文件
    if (file) {
        // 预览图片
        const reader = new FileReader();
        reader.onload = function(e) {
            imageShower.src = e.target.result; // 设置图片显示地址
            imageShower.alt = file.name; // 设置图片显示文本
        };
        reader.readAsDataURL(file); // 读取文件并转换为 Data URL
        console.log(file);

        // 创建 FormData 对象
        const formData = new FormData();
        formData.append('image', file); // 将图片文件添加到 FormData

        // 调用 API 保存图片
        try {
            const response = await fetch('http://127.0.0.1:5145/upload', {
                method: 'POST',
                body: formData,
            });

            if (response.ok) {
                const result = await response.json(); // 解析 JSON 响应
                console.log('图片上传成功:', result);
            } else {
                console.error('上传失败:', response.statusText);
            }
        } catch (error) {
            console.error('请求错误:', error);
        }
    } else {
        alert('请先选择一张图片');
    }
});