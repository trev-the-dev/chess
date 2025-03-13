# ♟️ Chess Game in Pygame  
A Python-based chess game using Pygame, with fully interactive piece movement, rule enforcement, and special moves.  

---

## 🚀 TODO Roadmap  

This project follows this roadmap to ensure a smooth development process. Follow along as the chess game evolves!  

---

### 🎨 **1️⃣ Set Up the Chessboard Display**  
- [X] 🖥 **Initialize Pygame** in `main.py`  ✅
- [X] 🎨 **Create game constants** (`WIDTH`, `HEIGHT`, etc.)  ✅
- [X] 🏁 **Set up board colors** (`LIGHT`, `DARK`)  ✅
- [X] 📏 **Write `draw_board()` function**  ✅
- [X] 🪟 **Create the game window**  ✅

---

### 🏇 **2️⃣ Load & Display Pieces**
- [ ]  **Load piece images** (store them in a dictionary and scale them)
- [X]  **Define a board representation** using a **2D list** of strings for now
- [X]  **Write `draw_pieces()` function** to place images on the board

---

### 🔧 **3️⃣ Create a `Piece` Base Class**  
- [ ] 📜 **Define `Piece` class** in `piece.py`

---

### ⚔️ **4️⃣ Implement Movement for Each Piece**  

#### 👑 **Major Pieces First**  
- [ ] 🏇 **`Knight` (`knight.py`)** → Moves in L-shapes 
- [ ] 🏗 **`Rook` (`rook.py`)** → Moves in straight lines  
- [ ] 🎭 **`Bishop` (`bishop.py`)** → Moves diagonally  
- [ ] 👸 **`Queen` (`queen.py`)** → Combines rook & bishop moves   
- [ ] 🤴 **`King` (`king.py`)** → Moves one square in any direction  

#### 🏰 **Then Pawns**  
- [ ] 🚶 **Implement `Pawn` class (`pawn.py`)**  
- [ ] 📜 **Define `valid_moves()` for pawns**  
- [ ] ✅ **Test pawn movement before proceeding**  

---

### 🖱 **5️⃣ Handle Player Interaction**  
- [ ] 🖲 **Handle mouse events for selection & movement**

---

### 📜 **6️⃣ Validate Moves & Enforce Rules**  
- [ ] ✅ **Allow only legal moves**  
- [ ] 🚫 **Prevent jumping (except knights)**  
- [ ] 🔄 **Enforce turn-based play (White first, then Black)**  

---

### 🎯 **7️⃣ Special Rules & Features**  
- [ ] 🔄 **Castling (king & rook)**  
- [ ] ♟️ **Pawn promotion**  
- [ ] 🏹 **En passant**  

---

### 🎨 **8️⃣ Final Enhancements**  
- [ ] 🔄 **Code refactoring**   
- [ ] 🔧 **Add computer logic**
- [ ] ♜ **Display captured pieces**  
- [ ] 🔄 **Add a restart button**  

---

## 🔧 How to Run the Game  
```bash
git clone https://github.com/trev-the-dev/chess.git
cd chess
python main.py
```
