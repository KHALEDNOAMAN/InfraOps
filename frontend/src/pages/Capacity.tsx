import React from 'react';
import { AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const data = Array.from({length: 20}).map((_, i) => ({
  month: `M${i+1}`,
  usage: 40 + (i * 2) + Math.random() * 5,
  predicted: i > 15 ? 40 + (i * 2) + Math.random() * 5 : null
}));

export default function Capacity() {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">Capacity Planning</h1>
      
      <div className="grid grid-cols-4 gap-6">
        {['CPU', 'Memory', 'Storage', 'Power'].map(res => (
          <div key={res} className="bg-gray-900 p-6 rounded-xl border border-gray-800">
            <h3 className="text-gray-400 mb-2">{res} Usage</h3>
            <div className="flex items-end gap-2">
              <span className="text-3xl font-bold">78%</span>
            </div>
            <div className="w-full bg-gray-800 h-2 mt-4 rounded-full overflow-hidden">
              <div className="bg-cyan-500 h-full w-[78%]"></div>
            </div>
          </div>
        ))}
      </div>

      <div className="bg-gray-900 p-6 rounded-xl border border-gray-800">
        <h2 className="text-lg font-medium mb-4">6-Month Forecast</h2>
        <div className="h-80">
          <ResponsiveContainer width="100%" height="100%">
            <AreaChart data={data}>
              <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
              <XAxis dataKey="month" stroke="#9CA3AF" />
              <YAxis stroke="#9CA3AF" />
              <Tooltip contentStyle={{ backgroundColor: '#1F2937', border: 'none' }} />
              <Area type="monotone" dataKey="usage" stroke="#22D3EE" fill="#0891B2" fillOpacity={0.3} />
              <Area type="monotone" dataKey="predicted" stroke="#A78BFA" strokeDasharray="5 5" fill="none" />
            </AreaChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
}
