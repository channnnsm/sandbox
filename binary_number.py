import { useState } from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';

const BinaryVisualizer = () => {
  const [decimal, setDecimal] = useState(0);
  
  // 10進数から2進数への変換
  const getBinary = (num) => {
    return num.toString(2).padStart(8, '0');
  };
  
  // 各ビットの値を計算
  const getBitValues = (binary) => {
    return binary.split('').map((bit, index) => {
      return bit === '1' ? Math.pow(2, 7-index) : 0;
    });
  };

  return (
    <Card className="w-full max-w-xl">
      <CardHeader>
        <CardTitle className="text-xl font-bold">二進数変換ビジュアライザー</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="space-y-6">
          <div className="flex items-center gap-4">
            <label className="font-medium">10進数:</label>
            <input
              type="number"
              min="0"
              max="255"
              value={decimal}
              onChange={(e) => setDecimal(Number(e.target.value) || 0)}
              className="border rounded px-2 py-1 w-24"
            />
          </div>

          <div className="space-y-4">
            <div className="grid grid-cols-8 gap-1">
              {getBinary(decimal).split('').map((bit, index) => (
                <div
                  key={index}
                  className={`p-4 text-center border rounded-lg ${
                    bit === '1' ? 'bg-blue-500 text-white' : 'bg-gray-100'
                  }`}
                >
                  {bit}
                </div>
              ))}
            </div>

            <div className="grid grid-cols-8 gap-1 text-sm text-center">
              {getBitValues(getBinary(decimal)).map((value, index) => (
                <div key={index} className="p-1">
                  {value || 0}
                </div>
              ))}
            </div>

            <div className="grid grid-cols-8 gap-1 text-sm text-center">
              {Array.from({ length: 8 }).map((_, index) => (
                <div key={index} className="p-1">
                  2<sup>{7-index}</sup>
                </div>
              ))}
            </div>
          </div>

          <div className="mt-4 p-4 bg-gray-50 rounded-lg">
            <p className="font-medium">説明:</p>
            <p>• 0から255までの数値を入力してください</p>
            <p>• 青いマスは1、白いマスは0を表します</p>
            <p>• 各位置の値は2のべき乗で計算されます</p>
          </div>
        </div>
      </CardContent>
    </Card>
  );
};

export default BinaryVisualizer;